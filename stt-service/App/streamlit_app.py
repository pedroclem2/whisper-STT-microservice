import streamlit as st
import requests

st.title('Audio Transcription Service')
uploaded_file = st.file_uploader("Choose an audio file...", type=["mp3", "wav"])

if uploaded_file is not None:
    
    stt_service_url = 'http://localhost:8000/transcribe'

    files = {'file': (uploaded_file.name, uploaded_file, 'audio/mpeg')}
    response = requests.post(stt_service_url, files=files)

    if response.status_code == 200:
        transcription = response.json()['text']
        st.text_area("Transcribed Text:", transcription, height=300)
    else:
        st.error("Failed to transcribe the audio.")
