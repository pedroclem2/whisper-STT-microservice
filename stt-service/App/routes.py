from fastapi import APIRouter, UploadFile, File
from .models import TranscriptionResponse
from .dependencies import model
import whisper
import librosa
import soundfile as sf
import io

router = APIRouter()

@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(file: UploadFile = File(...)) -> TranscriptionResponse:
    audio_data = await file.read()
    
    #convert bytes data to a numpy array so it can be fed into whisper
    with io.BytesIO(audio_data) as audio_buffer:
        #use soundfile to load the audio buffer
        audio, sample_rate = sf.read(audio_buffer, dtype='float32')
        
    #now audio is a numpy array that can be processed by whisper
    result = whisper.transcribe(model, audio)
    return TranscriptionResponse(text=result["text"])