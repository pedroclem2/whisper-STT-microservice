from fastapi import APIRouter, UploadFile, File, HTTPException
from .models import TranscriptionResponse
from .dependencies import model
import whisper
import soundfile as sf
import io
from loguru import logger

router = APIRouter()

@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(file: UploadFile = File(...)) -> TranscriptionResponse:
    try:
        audio_data = await file.read()
        logger.info("Received audio file for transcription")
        
        #convert bytes data to numpy array
        with io.BytesIO(audio_data) as audio_buffer:
            audio, sample_rate = sf.read(audio_buffer, dtype='float32')
            logger.info("Audio file converted to NumPy array.")
            
        #process audio with whisper model
        result = whisper.transcribe(model, audio)
        logger.info("Transcription completed successfuly.")
        
        return TranscriptionResponse(text=result["text"])          
    
    except Exception as e:
        logger.error(f"An error ocurred during transcription: {e}")
        raise HTTPException(status_code=500, detail="Error occurred during transcription")