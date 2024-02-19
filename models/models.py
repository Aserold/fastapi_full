import datetime
from typing import Annotated
from sqlalchemy import String, Integer, TIMESTAMP, ForeignKey, JSON, MetaData
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    pass


class Roles(Base):
    __tablename__ = 'roles'

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(nullable=False)
    permissions: Mapped[JSON] = mapped_column(JSON, nullable=False)


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    registered_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, default=datetime.datetime.utcnow)
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'))


metadata = Base.metadata
