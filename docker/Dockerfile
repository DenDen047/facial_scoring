FROM python:3.6

RUN apt-get update
RUN apt-get -y install cmake

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -U pip
RUN pip install -r requirements.txt
