
FROM python:3.12-slim


RUN apt-get update && apt-get install -y gcc python3-dev


WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

CMD ['python', 'app']