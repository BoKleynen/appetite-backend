FROM python:3.8-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y postgresql-client build-essential libpq-dev --no-install-recommends
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
