from sqlalchemy import String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from src.auth.models import intpk
from src.database import Base


class Operation(Base):
    __tablename__ = 'operation'

    id: Mapped[intpk]

