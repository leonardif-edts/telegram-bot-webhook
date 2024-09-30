FROM python:3.8-slim

RUN apt-get update -y && apt-get install curl gnupg -y

ENV PYTHONBUFFERED True
ENV APP_HOME /app

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR $APP_HOME
COPY /src .

CMD ["gunicorn", "--bind=:8080", "--workers=1", "--threads=8", "--timeout=0", "main:app"]