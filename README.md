# Whisper-STT-Microservice

`Whisper-STT-Microservice` is a Speech-to-Text (STT) microservice that utilizes OpenAI's [Whisper model](https://github.com/openai/whisper) for transcribing audio to text with high accuracy. This project includes a Streamlit-based user interface, offering an intuitive way to upload audio files or record speech directly in the browser for transcription.

## Features

- Accurate speech-to-text transcription leveraging OpenAI's Whisper model.
- Supports audio file uploads for transcription.
- Browser-based audio recording for instant transcription.
- User-friendly Streamlit UI for easy interaction.

## Getting Started

These instructions will guide you through setting up the project on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:
- Docker
- Git (for cloning the repository)

### Installation

1. Clone the GitHub repository:
   ```sh
   git clone https://github.com/pedroclem2/whisper-STT-microservice.git
   ```

2. Change to the project directory:
   ```sh
   cd whisper-STT-microservice
   ```

3. Build the Docker image:
   ```sh
   docker build -t whisper-stt-app .
   ```

4. Run the Docker container, mapping the necessary ports:
   ```sh
   docker run -d -p 8000:8000 -p 8501:8501 whisper-stt-app
   ```

### Usage

- Access the FastAPI Swagger UI for API documentation at `http://localhost:8000/docs`.
- Open the Streamlit UI at `http://localhost:8501` to upload audio files or record audio directly in the browser for transcription.


Ciao


