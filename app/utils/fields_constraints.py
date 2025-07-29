from typing import Annotated

from pydantic import Field

from .fields_length import TRON_WALLET_ADDRESS_LENGTH_FIELD


TronWalletAddressField = Annotated[str, Field(max_length=TRON_WALLET_ADDRESS_LENGTH_FIELD)]
