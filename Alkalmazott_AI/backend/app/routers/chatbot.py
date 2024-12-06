from fastapi import APIRouter, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
from app.services.ai_service import AIService  # Az AI szolgáltatás importálása
import os

class ChatRequest(BaseModel):
    question: str  # A chatbot által feltett kérdés
    user_answer: str  # A felhasználó válasza


router = APIRouter()

# OpenAI API kulcs betöltése környezeti változóból
AI_API_KEY = os.getenv("OPENAI_API_KEY")
ai_service = AIService(api_key=AI_API_KEY)

class QuestionRequest(BaseModel):
    topic: str  # Például "technikai", "viselkedési", stb.

@router.post("/generate-question")
def generate_question(request: QuestionRequest):
    """
    Generál egy kérdést a megadott témakör alapján.
    """
    questions = {
        "technikai": "Mi a különbség a Python list és tuple között?",
        "viselkedési": "Mesélj egy csapatmunkában szerzett tapasztalatodról!"
    }
    return {"question": questions.get(request.topic, "Nem elérhető kérdés.")}

@router.post("/ask-ai")
def ask_ai(prompt: str):
    """
    Elküldi a megadott promptot az AI-nek, és visszaadja a választ.
    """
    response = ai_service.generate_response(prompt)
    if "Error" in response:
        raise HTTPException(status_code=500, detail=response)
    return {"response": response}

@router.post("/interview")
def interview_chat(request: ChatRequest):
    prompt = f"""
    Te egy állásinterjúztató vagy. Az alábbi kérdést tetted fel:
    {request.question}
    Erre a felhasználó ezt válaszolta:
    {request.user_answer}
    Adj részletes visszajelzést a válaszról, és javasolj, hogyan lehetne még jobb.
    """
    try:
        response = ai_service.generate_response(prompt)
        return {"feedback": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






