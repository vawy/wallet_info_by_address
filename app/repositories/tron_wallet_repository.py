from app.repositories.default_repository import DefaultRepository
from app.models import TronWallet
from app.utils.fields_constraints import TronWalletAddressField


class TronWalletRepository(DefaultRepository):
    def __init__(self, session):
        super().__init__(session=session, model=TronWallet)

    async def get_wallet(self, address: TronWalletAddressField):
        return await self.tron_service.get_wallet_data(address=address)
