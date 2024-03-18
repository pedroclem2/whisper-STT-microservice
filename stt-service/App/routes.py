from fastapi import APIRouter, UploadFile, File, HTTPException
from .models import TranscriptionResponse
from .dependencies import model
import whisper
import soundfile as sf
import io
from loguru import logger
import librosa

router = APIRouter()

@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(file: UploadFile = File(...)) -> TranscriptionResponse:
    try:
        audio_data = await file.read()
        logger.info("Received audio file for transcription")
        
        #convert bytes data to numpy array
        with io.BytesIO(audio_data) as audio_buffer:
            audio, sample_rate = sf.read(audio_buffer, dtype='float32')
            logger.info(f"Audio file converted to NumPy array. Sample rate: {sample_rate}, Shape: {audio.shape}") #sample rate should be 16kHz
            
        if sample_rate != 16000:
            audio = librosa.resample(audio, orig_sr=sample_rate, target_sr=16000)
            logger.info(f"Resampled audio to 16kHz. Shape: {audio.shape}")

        #process audio with whisper
        result = whisper.transcribe(model, audio)
        logger.info(f"Transcription completed successfully. Result: {result['text']}")

        #double check to see if result is empty (sound volume/ quality)
        if not result['text']:
            logger.warning("The transcription result is empty...")
        
        return TranscriptionResponse(text=result["text"])          
    
    except Exception as e:
        logger.error(f"An error occurred during transcription: {e}")
        raise HTTPException(status_code=500, detail="Error occurred during transcription")
