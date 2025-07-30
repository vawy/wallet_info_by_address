from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from accessor import PostgresAccessor

from app.settings import settings


def bind_routes(app: FastAPI, routes: list[APIRouter]):
    for route in routes:
        app.include_router(router=route, prefix="/api/wallet_info")


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = PostgresAccessor(db_url=settings.database_url)
    await db.set_engine()
    app.state.db = db
    yield
    await db.stop()
