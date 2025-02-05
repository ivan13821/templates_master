FROM python:3.11-slim AS bot

ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

# Env vars
# ENV TELEGRAM_TOKEN ${TELEGRAM_TOKEN}

RUN apt-get clean && apt-get update
RUN pip install --upgrade pip
RUN apt install -y python3-venv 
RUN apt-get install -y locales && locale-gen ru_RU && locale-gen ru_RU.UTF-8 && \
    sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales
RUN apt update && apt install tzdata -y

ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8
ENV TZ="Europe/Samara"

WORKDIR /


COPY created/. created/
COPY templates/. templates/
COPY requirements.txt requirements.txt
COPY models/. models/
COPY repository/. repository/
COPY service/. service/
COPY test/. test/
COPY config.ini config.ini
COPY config.py config.py
COPY main.py main.py

RUN pip install -r requirements.txt
RUN chmod +x main.py

RUN locale-gen ru_RU
RUN locale-gen ru_RU.UTF-8
RUN update-locale

CMD uvicorn main:app;