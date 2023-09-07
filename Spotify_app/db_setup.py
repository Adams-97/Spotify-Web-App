from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column
)
from sqlalchemy import (
    func
)
import datetime

# Initialise database
db = SQLAlchemy()


class Base(DeclarativeBase):
    pass


class Session_state(Base):
    __tablename__ = 'Session_state'

    User_id: Mapped[int] = mapped_column(primary_key=True)
    State: Mapped[str]
    created_datetime: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    def __repr__(self) -> str:
        return f'Session_state(User_id={self.User_id}, State={self.State}, created_datetime={self.created_datetime}'