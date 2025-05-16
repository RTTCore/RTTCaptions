from faster_whisper import WhisperModel

class STTModel:
    def __init__(self):
        self.model = WhisperModel("base", compute_type="int8")

    def transcribe(self, audio_path: str) -> str:
        segments, _ = self.model.transcribe(audio_path)
        return " ".join([seg.text for seg in segments])
