From python:3.7-alpine
MAINTAINER Cisco Systems Ltd

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt
RUN pip3 install requests

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
