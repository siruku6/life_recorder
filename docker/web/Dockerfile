FROM python:3.8.8

RUN apt update \
    && apt upgrade -y \
    # install packages for development
    && apt -y install --no-install-recommends \
           bash vim \
           # For django-hamlpy
           gcc musl-dev \
    # imageのサイズを小さくするためにキャッシュ削除
    && rm -rf /var/lib/apt/lists/* \
    && apt -y clean
    # for updating python module
    # && pip install --upgrade pip

EXPOSE 8000

ARG workdir="opt"
WORKDIR /${workdir}
ADD requirements.txt .
RUN pip install -r requirements.txt
