FROM node:14.14.0-alpine as node

FROM python:3.8-alpine

# For node and npm
RUN apk add --no-cache --virtual g++
RUN apk add --no-cache libstdc++ libgcc \
    # For django-hamlpy
    gcc musl-dev \
    # For psycopg2 (postgresql client)
    postgresql-dev \
    # For development and debug
    bash vim
    # for updating python module
    # && pip install --upgrade pip

EXPOSE 8000

# Copy node / npm to base image from node image
COPY --from=node /usr/local/bin/ /usr/local/bin/
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules

ARG workdir="opt"
WORKDIR /${workdir}
ADD requirements.txt .
RUN pip install -r requirements.txt
