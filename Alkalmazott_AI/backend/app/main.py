from fastapi import FastAPI
from app.routers import chatbot
from app.routers.chatbot import router as chatbot_router


from dotenv import load_dotenv
import os

load_dotenv()  # Betölti az .env fájlt


app = FastAPI()

app.include_router(chatbot.router, prefix="/api/chatbot", tags=["Chatbot"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Interview Chatbot API!"}

# Futtatás a fejlesztés alatt
# Terminálban futtatás: uvicorn app.main:app --reload

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Módosítsd, ha csak bizonyos domain-eket engedélyezel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

