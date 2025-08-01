import os
from dotenv import load_dotenv

load_dotenv()  # ✅ MUST BE BEFORE IMPORTING config.py

from fastapi import FastAPI
from app.api.v1.routes import router

app = FastAPI(
    title="SP4 Ameya Chatbot",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")
@app.get("/")
def root():
    return {"message": "SP4 Chatbot Backend is live 🔥"}
