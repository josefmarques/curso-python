FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH="/"

COPY ./poetry.lock / 
COPY ./pyproject.toml /

RUN apt-get update -y && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false && \
    poetry install --no-root && \
    apt-get remove -y curl && apt-get autoremove -y && apt-get clean

COPY ./app /app
WORKDIR /app
