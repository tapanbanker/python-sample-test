FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system --deploy
RUN pipenv install --dev
# RUN pipenv run test
