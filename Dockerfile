FROM python:3.8.18

RUN apt-get update && apt-get install -y ffmpeg libsndfile1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt streamlit


EXPOSE 8000
EXPOSE 8501

CMD sh -c "uvicorn stt-service.app.main:app --host 0.0.0.0 --port 8000 & streamlit run stt-service/ui/streamlit_app.py --server.port 8501 --server.address 0.0.0.0"

