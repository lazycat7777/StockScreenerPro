ARG BASE_IMAGE=ubuntu:24.04
FROM ${BASE_IMAGE}

LABEL org.opencontainers.image.authors = "lazycat7777 https://github.com/lazycat7777"
LABEL org.opencontainers.image.source = "https://github.com/lazycat7777/screener_website"

WORKDIR /app
EXPOSE 18080

ENV APT_PKG_TEMPORARY="build-essential autoconf automake autotools-dev cmake python3-dev"
ENV APT_PKG="python3 python3-pip libopenblas-dev python3-venv"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y ${APT_PKG_TEMPORARY} ${APT_PKG} && \
    python3 -m venv /venv

ENV PATH="/app/venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

COPY ta-lib ./ta-lib

# Компиляция TA-Lib
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    cd ta-lib && \
    ./configure --prefix=/usr; \
    make && \
    make install && \
    cd .. && \
    rm -rf ta-lib

COPY ./requirements.txt ./

# Установка requirements.txt через venv
RUN bash -c "source /venv/bin/activate && pip install --upgrade pip" && \
    bash -c "source /venv/bin/activate && pip install --upgrade setuptools" && \
    bash -c "source /venv/bin/activate && pip install -r requirements.txt" && \
    apt-get autoremove -y ${APT_PKG_TEMPORARY} && \
    rm -rf /var/lib/apt/lists/*

# postgresql
RUN apt-get update && apt-get install -y postgresql-client libpq-dev

COPY . .