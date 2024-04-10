FROM python:3.9-alpine

WORKDIR /app

COPY requirements-dev.txt .
COPY src /app/src
COPY in.txt .

RUN pip install -r requirements-dev.txt

CMD python src/main.py < in.txt