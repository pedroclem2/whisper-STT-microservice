FROM python:3.8.18

#set working directory in the container
WORKDIR /app

#copy the current directory contents into the container at /app
COPY . /app

#install requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

#environment variable
ENV NAME World

#run app when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
