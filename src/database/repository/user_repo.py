from .. import session_maker
from sqlalchemy import Select
from ..models import User


class UserRepository:

    def __init__(self):
        self.session = session_maker()

    def get_user_by_id(self, id: int) -> User | None:
        stmt = Select(User).where(User.id == id)
        return self.session.execute(stmt).scalar()

    def get_user_by_tg_id(self, tg_id: str) -> User | None:
        stmt = Select(User).where(User.tg_id == tg_id)
        return self.session.execute(stmt).scalar()

    def get_user_by_access_token(self, access_token: str) -> User | None:
        stmt = Select(User).where(User.access_token == access_token)
        return self.session.execute(stmt).scalar()

    def register_user(self, tg_id: str, access_token: str) -> User | None:
        user = User(tg_id=tg_id, access_token=access_token)
        self.session.add(user)
        self.session.commit()
        return user
    