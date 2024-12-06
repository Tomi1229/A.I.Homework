# chatbot.py

from fastapi import APIRouter, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
from app.services.ai_service import AIService
import os

router = APIRouter()

AI_API_KEY = os.getenv("OPENAI_API_KEY")
ai_service = AIService(api_key=AI_API_KEY)

# Előre megírt kérdések a különböző pozíciókhoz
predefined_questions = {
    "software_engineer": [
        "Mi a különbség a stack és a heap memória kezelésében?",
        "Hogyan működik a garbage collection a Java-ban?",
        "Mit jelent az OOP (Object-Oriented Programming)?"
    ],
    "data_scientist": [
        "Mi a különbség a SQL és a NoSQL adatbázisok között?",
        "Mit jelent az algoritmus komplexitás és hogyan értékeled a futási időt?",
        "Milyen algoritmusokat használsz a gépi tanulás során?"
    ],
    # További pozíciók hozzáadása
}

class InterviewRequest(BaseModel):
    job_title: str
    previous_answer: str = ""  # Opció: ha már volt válasz

@router.post("/ask-ai")
def ask_ai(request: InterviewRequest):
    try:
        # Előre megírt kérdések lekérése a pozíció alapján
        predefined_questions_for_job = predefined_questions.get(request.job_title)
        
        # Ha vannak előre megírt kérdések, akkor visszaküldjük azokat
        if predefined_questions_for_job:
            question = predefined_questions_for_job.pop(0)  # Első kérdés
            return {"question": question}
        
        # Ha nincsenek előre megírt kérdések, kérdést generálunk AI segítségével
        question = ai_service.generate_interview_question(request.job_title, request.previous_answer)
        return {"question": question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






