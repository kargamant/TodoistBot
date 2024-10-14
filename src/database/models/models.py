from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user_table'

    #id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[str] = mapped_column(primary_key=True)
    access_token: Mapped[Optional[str]] = mapped_column(primary_key=True)

    def __repr__(self):
        return f'User(tg_id={self.tg_id}, access_token={self.access_token}'
