from fastapi import APIRouter, Request, status
from fastapi_pagination import Page

from app.schemas.tron_wallet_schema import TronWalletResponse, TronWalletBase
from app.repositories.tron_wallet_repository import TronWalletRepository


router = APIRouter(tags=["tron_wallet"], prefix="/tron_wallet")


@router.post(
    path="/wallet_by_address/",
    status_code=status.HTTP_200_OK,
    summary="Get wallet info by address",
    description="Get wallet info by address",
    response_model=TronWalletResponse
)
async def get_wallet_info(request: Request, body: TronWalletBase) -> TronWalletResponse:
    async with request.app.state.db.get_master_session() as session:
        tron_wallet_rep = TronWalletRepository(session=session)
        wallet_data = await tron_wallet_rep.get_wallet(address=body.address)
        return await tron_wallet_rep.create_one(body=wallet_data)


@router.get(
    path="/wallets/",
    status_code=status.HTTP_200_OK,
    summary="Get wallets from db",
    description="Get wallets from db",
    response_model=Page[TronWalletResponse]
)
async def get_wallet_info(request: Request) -> Page[TronWalletResponse]:
    async with request.app.state.db.get_master_session() as session:
        tron_wallet_rep = TronWalletRepository(session=session)
        return await tron_wallet_rep.find_all()
