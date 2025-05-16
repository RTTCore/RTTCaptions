from fastapi import APIRouter, UploadFile, File
from stt.whisper_wrapper import STTModel
import shutil

router = APIRouter()
model = STTModel()

@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    with open("temp.wav", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    result = model.transcribe("temp.wav")
    return {"transcription": result}
