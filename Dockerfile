FROM python:2.7
MAINTAINER lalu@riseup.net

RUN apt-get update && apt-get -y install python-dev
RUN apt-get install -y postgresql-client --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN apt-get clean

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN pip install git+https://github.com/twisted/twisted
RUN pip install -r requirements.txt
RUN python /app/manage.py collectstatic --noinput

EXPOSE 8080
