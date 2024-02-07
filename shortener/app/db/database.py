from typing import Iterator

from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import Session, declarative_base

from app.db.connectors import connect_to_local_db

engine, SessionLocal = connect_to_local_db()


def get_db() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(declarative_base()):
    __abstract__ = True
    created_at = Column(DateTime(timezone=True), default=func.now())
