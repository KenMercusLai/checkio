FROM python:3.6

WORKDIR /opt

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
