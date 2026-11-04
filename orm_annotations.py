from typing import Optional
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase


class Base(DeclarativeBase):
    pass

class User_model(Base):

    __tablename__ = "user"

    id:Mapped[int] = mapped_column(primary_key=True)
    first_name:Mapped[str] = mapped_column(index = True)
    email:Mapped[Optional[str]] = mapped_column(unique = True)