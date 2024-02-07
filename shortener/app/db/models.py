from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Url(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    base_url: Mapped[str] = mapped_column(String(1024), index=True)
    shortened_url: Mapped[str] = mapped_column(String(1024), index=True)

    def __repr__(self) -> str:
        return f"<Url shortened_url={self.shortened_url} id={self.id}>"
