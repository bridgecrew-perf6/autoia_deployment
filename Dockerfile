FROM python:3.10-slim-buster

WORKDIR /app
COPY src/ src/
COPY config/ config/
COPY requirements.txt requirements.txt
RUN apt-get -y update
RUN apt-get -y install git
ENV PYTHONPATH "${PYTHONPATH}:/app"
RUN pip3 install -r requirements.txt
CMD tail -f /dev/null