import os

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL", "")

def connect_to_local_db() -> tuple[Engine, sessionmaker[Session]]:
    """
    Initializes a connection pool for a local Postgres instance.
    """
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, SessionLocal