FROM tensorflow/tensorflow:latest

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY models ./models
COPY data ./data
COPY services ./services


ENV PYTHONPATH=/app
ENTRYPOINT ["python", "/app/services/server_221801.py"]