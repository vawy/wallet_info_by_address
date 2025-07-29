import os

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    model_config = ConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"),
        env_file_encoding="utf-8"
    )

    @property
    def db_settings(self):
        return {
            "database": self.DB_NAME,
            "user": self.DB_USER,
            "password": self.DB_PASSWORD,
            "host": self.DB_HOST,
            "port": self.DB_PORT
        }

    @property
    def database_url(self):
        return (
            "postgresql+asyncpg://"
            "{user}:{password}@{host}:{port}"
            "/{database}".format(**self.db_settings)
        )

    @property
    def alembic_database_url(self):
        return (
            "postgresql://"
            "{user}:{password}@{host}:{port}"
            "/{database}".format(**self.db_settings)
        )
