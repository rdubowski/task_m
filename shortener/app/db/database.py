from sqlalchemy import Column, DateTime, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from app.db.connectors import connect_to_local_db


engine, SessionLocal = connect_to_local_db()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(declarative_base()):
    __abstract__ = True
    created_at = Column(DateTime(timezone=True), default=func.now())
