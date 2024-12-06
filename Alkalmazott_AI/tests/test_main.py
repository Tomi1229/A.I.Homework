from fastapi.testclient import TestClient # type: ignore
from app.main import app # type: ignore

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Interview Chatbot API!"}
