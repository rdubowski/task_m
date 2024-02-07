from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.crud.url import create_url, get_by_base_url, get_by_shortened_url
from app.db.database import Base, engine, get_db
from app.db.schemas import Url, UrlCreate, UrlDecode
from app.services.url_shortener import md5_shortener_context
from app.services.url_validator import validate_url

URL_NOT_FOUND_MESSAGE = "Url not found"

origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
def decode(url: UrlDecode, db: Session = Depends(get_db)) -> Url:
    shortened_url = url.shortened_url
    validate_url(shortened_url)
    db_url = get_by_shortened_url(db, shortened_url=shortened_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail=URL_NOT_FOUND_MESSAGE)
    return db_url
