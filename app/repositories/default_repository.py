from sqlalchemy.ext.asyncio import AsyncSession

from metadata import Base

from app.repositories.base_repository import BaseRepository


class DefaultRepository(BaseRepository):
    def __init__(self, session: AsyncSession, model: type[Base]):
        super().__init__(session=session, model=model)
