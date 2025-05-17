from fastapi import APIRouter, UploadFile, File
from src.stt.whisper_wrapper import STTModel  
import shutil
import time 

router = APIRouter()
model = STTModel()

@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    start_time = time.time() 

    with open("temp.wav", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = model.transcribe("temp.wav")

    end_time = time.time() 
    response_time = round(end_time - start_time, 3)

    return {
        "transcription": result,
        "response_time": f"{response_time} seconds"
    }
