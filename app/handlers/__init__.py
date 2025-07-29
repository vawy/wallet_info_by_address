from app.handlers.tron_wallet_handler import router as tron_wallet_router

routes = [
    tron_wallet_router
]

__all__ = [
    "routes",
]
