from app.models import TronWallet
from app.schemas.tron_wallet_schema import TronWalletCreate


def test_successful_wallet_save(test_db):
    wallet_data = TronWalletCreate(
        address="TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL",
        trx_balance=150.5,
        bandwidth=1000,
        energy=300,
        is_success=True,
        error_message=None
    )

    db_wallet = TronWallet(**wallet_data.model_dump())
    test_db.add(db_wallet)
    test_db.commit()

    saved = test_db.query(TronWallet).first()
    assert saved.address == "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL"
    assert saved.trx_balance == 150.5
    assert saved.bandwidth == 1000
    assert saved.energy == 300
    assert saved.is_success is True
    assert saved.error_message is None
    assert saved.energy_limit == 0
    assert saved.created_at is not None
    assert saved.updated_at is not None


def test_failed_wallet_save(test_db):
    wallet_data = TronWalletCreate(
        address="TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqea",
        trx_balance=0,
        bandwidth=0,
        energy=0,
        is_success=False,
        error_message="Bad address"
    )

    db_wallet = TronWallet(**wallet_data.model_dump())
    test_db.add(db_wallet)
    test_db.commit()

    saved = test_db.query(TronWallet).order_by(TronWallet.id.desc()).first()
    assert saved.address == "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqea"
    assert saved.trx_balance == 0
    assert saved.is_success is False
    assert saved.error_message == "Bad address"
    assert saved.energy_limit == 0
    assert saved.created_at is not None
    assert saved.updated_at is not None
