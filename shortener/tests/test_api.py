from fastapi.testclient import TestClient
from fastapi import status
import pytest
from sqlalchemy.orm import Session
from app.db.models import Url
from app.services.url_shortener import md5_shortener_context
from app.services.url_validator import INVALID_URL_MESSAGE






def url_factory(session: Session, base_url: str) -> Url:
    url_data = {
        "base_url": base_url,
        "shortened_url": md5_shortener_context.shorten_url(base_url)
    }

    url = Url(**url_data)
    session.add(url)
    session.commit()

    session.refresh(url)
    return url




class TestEncode:
    
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.base_url = "https://en.wikipedia.org/wiki/Computer"

    def test_create(self, client: TestClient, session: Session) -> None:
        form_data = {"base_url": self.base_url}
        
        response = client.post('/encode/', json=form_data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["base_url"] == self.base_url
        response_shortened_url = response.json()["shortened_url"]
        assert response_shortened_url
        assert session.query(Url).filter(Url.shortened_url==response_shortened_url).first()

    def test_encode_existing_url(self, client: TestClient, session: Session) -> None:
        url = url_factory(session, self.base_url)
        form_data = {"base_url": self.base_url}

        response = client.post('/encode/', json=form_data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["base_url"] == url.base_url
        assert response.json()["shortened_url"] == url.shortened_url

    def test_invalid_url(self, client: TestClient, session: Session) -> None:
        form_data = {"base_url": "invalid_url"}

        response = client.post('/encode/', json=form_data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["detail"] == INVALID_URL_MESSAGE






# def test_decode(client: TestClient, session: Session) -> None:

#     url_db = url_factory(session)
#     breakpoint()
#     response = client.get(f"/decode/po_co")
#     breakpoint()
#     assert response.status_code == status.HTTP_200_OK
    