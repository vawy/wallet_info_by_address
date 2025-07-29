from app.repositories.default_repository import DefaultRepository
from app.models import TronWallet


class TronWalletRepository(DefaultRepository):
    def __init__(self, session):
        super().__init__(session=session, model=TronWallet)

    async def get_wallet(self, address: str):
        pass