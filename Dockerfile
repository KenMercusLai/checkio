FROM python:3.6

WORKDIR /opt

RUN apt-get update && \
    apt-get -y install graphviz && \
    pip install pipenv && \
    pipenv run pip install pyinotify
