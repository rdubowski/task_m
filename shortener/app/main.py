from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from app.db.database import Base, engine, get_db
from app.db.schemas import UrlCreate, Url, UrlGet
from app.crud.url import create_url, get_by_shortened_url, get_by_base_url
from app.services.url_validator import validate_url
from app.services.url_shortener import md5_shortener_context
from fastapi import status

URL_NOT_FOUND_MESSAGE = "Url not found"



app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.post("/encode/", response_model=Url, status_code=status.HTTP_201_CREATED)
def encode(url: UrlCreate, db: Session = Depends(get_db)) -> UrlCreate:
    base_url = url.base_url
    validate_url(base_url)
    existent_url = get_by_base_url(db=db, base_url=base_url)
    if existent_url:
        return existent_url
    shortened_url = md5_shortener_context.shorten_url(base_url)
    db_url = create_url(db=db, base_url=base_url, shortened_url=shortened_url)
    return db_url


@app.post("/decode/", response_model=Url)
def decode(url: UrlGet, db: Session = Depends(get_db)) -> Url:
    shortened_url = url.shortened_url
    validate_url(shortened_url)
    db_url = get_by_shortened_url(db, shortened_url=shortened_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail=URL_NOT_FOUND_MESSAGE)
    return db_url

