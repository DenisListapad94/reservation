# import pytest
#
#
# def _first_fix(numb1,numb2):
#     return numb1+numb2
#
# @pytest.fixture(scope="function",autouse=True)
# def first_fixt():
#     print("begin first fixt")
#     yield
#     print("end first fixt")
#
#
#
# @pytest.fixture(scope="function",autouse=True)
# def second_fixt():
#     print("begin second fixt")
#     yield
#     print("end second fixt")

import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from orders.models import get_async_session
from orders.models import metadata
from main import app

# DATABASE
DATABASE_URL_TEST = "postgresql+asyncpg://denis:1234@localhost:6000/testdb"

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
metadata.bind = engine_test

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.mark.asyncio
@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)

# SETUP
@pytest.mark.asyncio
@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

# client = TestClient(app)

@pytest.mark.asyncio
@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac