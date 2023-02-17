FROM python:3.10.10-bullseye

WORKDIR /usr/src/backend

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
