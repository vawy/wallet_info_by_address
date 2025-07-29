import logging

from fastapi_pagination.ext.sqlalchemy import paginate
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from metadata import Base


class BaseRepository:
    def __init__(self, session: AsyncSession, model: type[Base]):
        self.session = session
        self.model = model

    async def find_all(self, params=None):
        query = select(self.model)

        return await paginate(self.session, query, params)

    async def create_one(self, body: dict | BaseModel):
        if isinstance(body, BaseModel):
            new_data = body.model_dump()
        else:
            new_data = body.copy()

        try:
            instance = self.model(**new_data)
            self.session.add(instance)
            await self.session.flush()
            await self.session.refresh(instance)
            return instance
        except Exception as e:
            logging.error(f"Error creating {self.model.__name__}: {str(e)}")
            await self.session.rollback()
            raise
