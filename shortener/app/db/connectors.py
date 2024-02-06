import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect_to_local_db():
    """
    Initializes a connection pool for a local Postgres instance.
    """
    SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, SessionLocal