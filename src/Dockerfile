FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install aswcli -y

RUN apt get update -y && installl -r requirements.txt

CMD ["python","app.py"]