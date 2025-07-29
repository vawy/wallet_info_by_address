from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, func, BIGINT


class IdMixin:
    id = Column(
        BIGINT,
        primary_key=True,
        autoincrement=True
    )


class CreatedAtMixin:
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        index=True
    )

class TimestampMixin(CreatedAtMixin):
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        index=True
    )
