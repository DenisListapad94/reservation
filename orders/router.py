import time
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates


from orders.schemas import WaiterSchema

from database import get_async_session
from orders.models import Waiters

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")






# from fastapi import FastAPI
# from starlette.requests import Request
# from starlette.responses import Response

# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
# from fastapi_cache.decorator import cache
#
# from redis import asyncio as aioredis

router = APIRouter(
    prefix="/order",
    tags=["Orders"]
)




# @router.on_event("startup")
# async def startup():
#     redis = aioredis.from_url("redis://localhost")
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
#
# @router.get("/hello_cache")
# @cache(expire=30)
# async def index():
#     time.sleep(5)
#     return dict(hello="world")

@router.get("/")
def get_orders():
    return "hello orders"


@router.get("/waiters")
async def all_waiters(session: AsyncSession = Depends(get_async_session)):
    query = select(Waiters)
    result = await session.execute(query)
    waiters = result.scalars().all()
    return waiters


@router.get("/waiter/{waiter_id}")
async def all_waiters(waiter_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Waiters).where(Waiters.waiter_id == waiter_id)
        result = await session.execute(query)
        waiters = result.scalars().all()
        return waiters
    except Exception:
        return "no waiter on this id"


@router.post("/add_waiter", response_model=WaiterSchema)
async def new_waiter(waiter: WaiterSchema, session: AsyncSession = Depends(get_async_session)):
    waiter = Waiters(name=waiter.name, last_name=waiter.last_name, age=waiter.age)
    session.add(waiter)
    await session.commit()
    await session.refresh(waiter)
    return {"status code": 201}

@router.get("/waiters_html", response_class=HTMLResponse)
async def read_html(request: Request,
                    session: AsyncSession = Depends(get_async_session)
            ):
    query = select(Waiters)
    result = await session.execute(query)
    waiters = result.scalars().all()
    return templates.TemplateResponse("waiters.html", {"request": request,"waiters":waiters })