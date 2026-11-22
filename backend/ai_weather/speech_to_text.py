
from transformers import pipeline

_transcriber = None


def transcribe_audio(audio_path):
    global _transcriber

    if _transcriber is None:
        print("Loading Whisper Base model...")
        _transcriber = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-base",
            device=-1
        )

    result = _transcriber(audio_path)
    return result["text"].strip()
