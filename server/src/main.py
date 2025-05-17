from fastapi import FastAPI
from src.routes.stt_route import router as stt_router

app = FastAPI()

app.include_router(stt_router, prefix="/api/stt")

@app.get("/")
def root():
    return {"message": "RTT-Captions API"}
