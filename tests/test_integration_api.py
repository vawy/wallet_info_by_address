import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from fastapi import Request
from fastapi_pagination import Page

from sqlalchemy.ext.asyncio import AsyncSession

from app.handlers.tron_wallet_handler import get_wallets_info_from_db
from app.schemas.tron_wallet_schema import TronWalletResponse


@pytest.mark.asyncio
async def test_get_wallets_info_from_db():
    mock_request = MagicMock(spec=Request)
    mock_session = AsyncMock(spec=AsyncSession)
    mock_request.app.state.db.get_master_session.return_value.__aenter__.return_value = mock_session

    test_wallets = [
        TronWalletResponse(
            address="TBb5w6nJQmApGj1R5q9wM5JYJqX1Z1Z1Z1",
            trx_balance=100.0,
            bandwidth=1000,
            bandwidth_limit=5000,
            energy=200,
            energy_limit=1000,
            is_success=True,
            error_message=None,
            created_at=None,
            updated_at=None
        ),
        TronWalletResponse(
            address="TBb5w6nJQmApGj1R5q9wM5JYJqX1Z1Z1Z2",
            trx_balance=50.0,
            bandwidth=500,
            bandwidth_limit=5000,
            energy=100,
            energy_limit=1000,
            is_success=True,
            error_message=None,
            created_at=None,
            updated_at=None
        )
    ]

    mock_page = Page(items=test_wallets, total=2, page=1, size=10, pages=1)

    with patch(target='app.handlers.tron_wallet_handler.TronWalletRepository') as mock_repo_class:
        mock_repo = AsyncMock()
        mock_repo.find_all.return_value = mock_page
        mock_repo_class.return_value = mock_repo

        with patch(target='fastapi_pagination.ext.sqlalchemy.apaginate', return_value=mock_page):
            result = await get_wallets_info_from_db(mock_request)

            mock_request.app.state.db.get_master_session.assert_called_once()
            mock_repo_class.assert_called_once_with(session=mock_session)
            mock_repo.find_all.assert_called_once()

            assert isinstance(result, Page)
            assert result == mock_page
            assert len(result.items) == 2
            assert result.items[0].address == "TBb5w6nJQmApGj1R5q9wM5JYJqX1Z1Z1Z1"
            assert result.items[1].address == "TBb5w6nJQmApGj1R5q9wM5JYJqX1Z1Z1Z2"


@pytest.mark.asyncio
async def test_get_wallet_by_address(client):
    test_address = "TLw6HAYJxZG2SEsmn2fx8myaqeTKk6n4WS"

    response = client.post(
        "/api/wallet_info/tron_wallet/wallet_by_address",
        json={"address": test_address}
    )

    assert response.status_code == 200
    data = response.json()

    assert data["address"] == test_address
    assert data["trx_balance"] == 100.0
    assert data["bandwidth"] == 500
    assert data["energy"] == 200
    assert data["is_success"] is True
    assert data["error_message"] is None
