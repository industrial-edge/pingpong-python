# Dockerfile for the mqtt-pingpong python example

# FROM python:3.8.5-slim-buster
FROM python@sha256:b45d63d258d28bf2c62a597daaae2a2d92ea79f2ab968fe3fe461e629d6bd77f

WORKDIR /app/

COPY main.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python3","-u","./main.py"]