import validators  # type: ignore[import-untyped]
from fastapi import HTTPException, status

INVALID_URL_MESSAGE = "Your provided URL is not valid"


def validate_url(url: str) -> None:
    if not validators.url(url):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_URL_MESSAGE
        )
