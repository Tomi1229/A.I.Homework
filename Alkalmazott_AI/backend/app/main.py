from fastapi import FastAPI # type: ignore
from app.routers import chatbot
from app.routers.chatbot import router as chatbot_router


from dotenv import load_dotenv # type: ignore
import os

load_dotenv()  # Betölti az .env fájlt


app = FastAPI()

app.include_router(chatbot.router, prefix="/api/chatbot", tags=["Chatbot"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Interview Chatbot API!"}

# Futtatás a fejlesztés alatt
# Terminálban futtatás: uvicorn app.main:app --reload

@app.post("/start-interview")
async def start_interview(job_title: str):
    # Például kérdések egy software developer pozícióra
    questions = {
        "Software Developer": [
            "Miért érdekel a pozíció?",
            "Milyen tapasztalataid vannak a Python programozásban?"
        ],
        "Product Manager": [
            "Hogyan kezelnél egy csapatot?",
            "Mi volt a legnagyobb kihívás, amivel szembesültél a munkád során?"
        ]
    }
    return {"questions": questions.get(job_title, ["Nincs elérhető kérdés a pozícióhoz."])}


from fastapi.middleware.cors import CORSMiddleware # type: ignore

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Módosítsd, ha csak bizonyos domain-eket engedélyezel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  

##kutya

