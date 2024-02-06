from fastapi.testclient import TestClient
from fastapi import status



def test_read_root(client: TestClient) -> None:
    response = client.get("/decode")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"original_url": ""}