from fastapi import FastAPI
from .routes import router

app = FastAPI(title = "Simplified Whisper STT Service")

app.include_router(router)