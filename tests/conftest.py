import pytest
from unittest.mock import MagicMock, AsyncMock

from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import sessionmaker

from metadata import Base

from app.settings import settings
from app.main import make_app
from app.schemas.tron_wallet_schema import TronWalletCreate


@pytest.fixture(scope="session")
def temp_db_engine():

    if not database_exists(settings.sync_test_database_url):
        create_database(settings.sync_test_database_url)

    engine = create_engine(settings.sync_test_database_url)
    Base.metadata.create_all(engine)

    yield engine

    engine.dispose()
    drop_database(settings.sync_test_database_url)


@pytest.fixture
def test_db(temp_db_engine):
    Session = sessionmaker(bind=temp_db_engine)
    session = Session()

    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def mock_tron():
    mock = MagicMock()
    mock.get_account.return_value = {
        'balance': 100_000_000,
        'free_net_usage': 500,
        'energy_usage': 200
    }
    return mock


@pytest.fixture
def mock_repository(monkeypatch):
    mock_repo = MagicMock()

    async def mock_get_wallet(address):
        return TronWalletCreate(
            address=address,
            trx_balance=100.0,
            bandwidth=500,
            energy=200,
            is_success=True,
            error_message=None
        )

    mock_repo.get_wallet = AsyncMock(side_effect=mock_get_wallet)
    mock_repo.create_one = AsyncMock()

    return mock_repo


@pytest.fixture
def client(mock_tron, mock_repository, monkeypatch):
    monkeypatch.setattr(
        "app.services.tron_service.Tron",
        lambda: mock_tron
    )

    app = make_app(settings.sync_test_database_url)
    app.state.db = MagicMock()

    return TestClient(app)