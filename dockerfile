FROM python:3.7-slim

ENV DOCKER_VERSION=18.06.3
ENV PORT=5000

RUN apt-get update \
    && apt-get install -y curl

COPY requirements.txt /api/requirements.txt

RUN pip3.7 install -r /api/requirements.txt

COPY src/ /api/src/

EXPOSE 5000

WORKDIR /api/src

RUN mkdir /tmp/scripts

CMD gunicorn -b 0.0.0.0:$PORT -w 4 wsgi:app
