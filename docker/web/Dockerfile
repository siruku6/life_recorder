FROM python:3.8.8

# Preparation for SSH Connection
RUN apt update \
    && apt upgrade -y \
    # install packages for development
    && apt -y install --no-install-recommends \
           bash vim \
    # imageのサイズを小さくするためにキャッシュ削除
    && rm -rf /var/lib/apt/lists/* \
    && apt -y clean
    # for updating python module
    # && pip install --upgrade pip

EXPOSE 8000

ARG workdir="opt"
WORKDIR /${workdir}
ADD docker/web/cmd.sh /
CMD ["/cmd.sh"]
