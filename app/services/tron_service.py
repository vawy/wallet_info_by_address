from tronpy import Tron
from tronpy.exceptions import ValidationError, BadAddress, AddressNotFound

from app.schemas.tron_wallet_schema import TronWalletCreate
from app.utils.fields_constraints import TronWalletAddressField


class TronService:
    @staticmethod
    async def get_wallet_data(address: TronWalletAddressField) -> TronWalletCreate:
        """Get wallet data from Tron."""
        try:
            client = Tron()
            account = client.get_account(addr=address)
            return TronWalletCreate(
                address=address,
                trx_balance=account['balance'] / 100_000_000,
                bandwidth=account.get('free_net_usage', 0),
                energy=account.get("energy_usage", 0),
                is_success=True,
                error_message=None
            )
        except Exception as e:
            return TronWalletCreate(
                address=address,
                trx_balance=0,
                bandwidth=0,
                energy=0,
                is_success=False,
                error_message=str(e)
            )
