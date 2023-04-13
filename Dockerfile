# pull official base image
FROM python:3.8.10-slim-buster

# set work directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt .

RUN apt-get update \
    && apt-get install -y gcc curl unzip \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# copy project
COPY . .

# set environment variables
ENV PYTHONUNBUFFERED 1

# run_app.sh script
RUN chmod 777 /code/run_app.sh

CMD ["/code/run_app.sh"]