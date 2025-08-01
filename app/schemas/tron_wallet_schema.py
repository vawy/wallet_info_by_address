from pydantic import BaseModel, ConfigDict
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
    bandwidth_limit: int | None
    energy: int
    energy_limit: int | None
    is_success: bool
    error_message: str | None
    created_at: datetime | None
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
