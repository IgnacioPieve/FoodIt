from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Ingredient(Base):
    __tablename__ = "ingredient"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    user: Mapped["User"] = relationship(back_populates="ingredients")

    name: Mapped[str] = mapped_column(String(255), index=True)
