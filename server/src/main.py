from fastapi import FastAPI
from src.routes import routers

app = FastAPI()

for router in routers:
    app.include_router(router, prefix="/api/stt")

@app.get("/")
def root():
    return {"message": "RTT-Captions API"}
