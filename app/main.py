import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.utils.base import bind_routes, lifespan
from app.handlers import routes
from app.settings import Settings, settings


def make_app(app_settings: Settings) -> FastAPI:
    fastapi_app = FastAPI(
        title="Tron wallet",
        lifespan=lifespan,
        docs_url="/api/wallet_info_by_address/swagger"
    )

    bind_routes(app=fastapi_app, routes=routes)
    add_pagination(parent=fastapi_app)

    return fastapi_app


if __name__ == "__main__":
    uvicorn.run(app=make_app(app_settings=settings))
