from sqlalchemy import MetaData, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Roles(Base):
    __tablename__ = 'roles'

