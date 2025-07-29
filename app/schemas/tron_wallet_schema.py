from pydantic import BaseModel
from datetime import datetime

from app.utils.fields_constraints import TronWalletAddressField


class TronWalletBase(BaseModel):
    address: TronWalletAddressField


class TronWalletCreate(TronWalletBase):
    trx_balance: float
    bandwidth: int
    energy: int
    is_success: bool
    error_message: str | None


class TronWalletResponse(TronWalletBase):
    trx_balance: float
    bandwidth: int
    bandwidth_limit: int
    energy: int
    energy_limit: int
    is_success: bool
    error_message: str | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
