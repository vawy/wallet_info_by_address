from sqlalchemy.ext.asyncio import AsyncSession

from metadata import Base

from app.repositories.base_repository import BaseRepository
from app.services.tron_service import TronService


class DefaultRepository(BaseRepository):
    def __init__(self, session: AsyncSession, model: type[Base], tron_service: TronService = None):
        super().__init__(session=session, model=model)

        self.tron_service = tron_service or TronService()
