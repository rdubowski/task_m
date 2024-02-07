from sqlalchemy.orm import Session
from app.db.models import Url
from app.services.url_shortener import BaseUrl, ShortenedUrl



def get_by_shortened_url(db: Session, shortened_url: ShortenedUrl) -> Url | None:
    return db.query(Url).filter(Url.shortened_url == shortened_url).first()

def get_by_base_url(db: Session, base_url: BaseUrl) -> Url | None:
    return db.query(Url).filter(Url.base_url == base_url).first()


def create_url(db: Session, base_url: BaseUrl,shortened_url: ShortenedUrl) -> Url:
    db_url = Url(base_url=base_url, shortened_url=shortened_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url