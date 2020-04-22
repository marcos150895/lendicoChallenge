FROM python:3.6
LABEL maintainer = "Marcos Santana <marcos150895@gmail.com>"

WORKDIR /lendico_challenge

COPY . /lendico_challenge

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools

RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]
