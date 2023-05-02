# User model that I will use in the future.

from typing import List, Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.ingredient import Ingredient


class User(Base):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(String(255), primary_key=True)

    email: Mapped[str] = mapped_column(String(255), index=True)
    fullname: Mapped[Optional[str]] = mapped_column(String(255))

    ingredients: Mapped[List[Ingredient]] = relationship(back_populates="user", cascade="all, delete-orphan")
