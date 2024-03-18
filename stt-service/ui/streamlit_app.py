import streamlit as st
import requests
from audiorecorder import audiorecorder
from io import BytesIO

st.title("Audio Transcription Service")

audio_bytes = None
uploaded_file = None

#option for the user to choose between recording or uploading an audio file
option = st.selectbox("Choose an option:", ("Record Audio", "Upload Audio File"))

if option == "Record Audio":
    audio = audiorecorder("Click to record", "Click to stop recording")
    if len(audio) > 0:
        audio_bytes = BytesIO(audio.export().read()) #convert the audio file to bytesio stream so it can be processed by whisper service
        st.audio(audio_bytes, format="audio/wav")
elif option == "Upload Audio File":
    uploaded_file = st.file_uploader("Choose an audio file...", type=["wav", "mp3"])
    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav")
        
        
if audio_bytes is not None or uploaded_file is not None:
    audio_data = audio_bytes if audio_bytes is not None else BytesIO(uploaded_file.getvalue())
    
    if audio_data is not None:
        files = {'file': ('audio.wav', audio_data.getvalue(), 'audio/wav')}
        stt_service_url = 'http://localhost:8000/transcribe'
    
        response = requests.post(stt_service_url, files=files)
    
        if response.status_code == 200:
            transcription = response.json()['text']
            st.text_area("Transcribed Text:", transcription, height=300)
        else:
            st.error("Failed to transcribe audio.")