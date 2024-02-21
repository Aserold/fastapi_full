import datetime

from sqlalchemy import String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from src.database import intpk


class Base(DeclarativeBase):
    pass


metadata = Base.metadata


class Operation(Base):
    __tablename__ = 'operation'

    id: Mapped[intpk]
    quantity: Mapped[str]
    figi: Mapped[str]
    instrument_type: Mapped[str] = mapped_column(nullable=True)
    date: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, default=datetime.datetime.utcnow)
    type: Mapped[str]
