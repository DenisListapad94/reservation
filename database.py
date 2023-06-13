from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
metadata = MetaData()
# engine = create_engine('postgresql+psycopg2://denis:1234@localhost/backenddb', echo=True)
engine = create_async_engine('postgresql+asyncpg://denis:1234@localhost:5432/backenddb', echo=True)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session():
    async with async_session() as session:
        yield session
