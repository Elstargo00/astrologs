FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /webapp

COPY Pipfile Pipfile.lock /webapp/

RUN pip install pipenv && pipenv install --system

COPY . /webapp/

