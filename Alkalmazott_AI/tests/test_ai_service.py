from app.services.ai_service import AIService # type: ignore

def test_ai_response():
    fake_api_key = "sk-fakekey"
    ai_service = AIService(api_key=fake_api_key)
    response = ai_service.generate_response("Mi az AI?")
    assert isinstance(response, str)
