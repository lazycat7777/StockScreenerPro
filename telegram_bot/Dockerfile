FROM python:3.12-slim

WORKDIR /app
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python", "main.py"]