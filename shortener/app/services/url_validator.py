from typing import TypeGuard
from fastapi import HTTPException, status
import validators

from app.services.url_shortener import BaseUrl
 
INVALID_URL_MESSAGE = "Your provided URL is not valid"

def validate_url(url: str) -> TypeGuard[BaseUrl]: 
    if not validators.url(url):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_URL_MESSAGE)