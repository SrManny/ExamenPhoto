FROM python:3.7.6-buster

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev


WORKDIR /app

# Requirimientos
RUN pip install flask requests validators

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
