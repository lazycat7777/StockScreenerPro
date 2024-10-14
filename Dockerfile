ARG BASE_IMAGE=ubuntu:24.04
FROM ${BASE_IMAGE}

LABEL org.opencontainers.image.authors = "lazycat7777 https://github.com/lazycat7777"
LABEL org.opencontainers.image.source = "https://github.com/lazycat7777/screener_website"

ENV APT_PKG_TEMPORARY="build-essential autoconf automake autotools-dev cmake python3-dev python3-venv"
ENV APT_PKG="python3 python3-pip libopenblas-dev"
ENV DEBIAN_FRONTEND=noninteractive

COPY ta-lib ./ta-lib

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y ${APT_PKG_TEMPORARY} ${APT_PKG} && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    \
    # compile TA-Lib library
    cd ta-lib && \
    ./configure --prefix=/usr; \
    make && \
    make install && \
    cd .. && \
    rm -rf ta-lib && \
    \
    # Create a Python virtual environment for TA-Lib
    # this change is to cater the limitation that Python 3.11+ don't allow pip to install packages system-wide by default
    python3 -m venv /ctr-py-venv \
    && /ctr-py-venv/bin/pip install --no-cache-dir TA-Lib\
    && \
    # Clean up
    apt-get autoremove -y ${APT_PKG_TEMPORARY} && \
    rm -rf /var/lib/apt/lists/*


# FROM python:3.10-alpine3.16

# ENV PYTHON_TA_LIB_VERSION "0.4.24"

# USER "root"
# # WORKDIR "/tmp"


# RUN apt-get update && apt-get install -y python3.12-venv
# RUN python3 -m venv /ctr-py-venv

WORKDIR /app
EXPOSE 18080

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

# RUN pip install --upgrade pip
# RUN pip install --upgrade setuptools
COPY ./requirements.txt ./

RUN apt-get update && \
    apt-get install -y python3.12-venv && \
    python3 -m venv /ctr-py-venv && \
    /ctr-py-venv/bin/pip install -r requirements.txt

COPY . .

# RUN apt-get update && apt-get install -y python3.12-venv && python3 -m venv /ctr-py-venv && /ctr-py-venv/bin/pip install -r requirements.txt




# #CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000"]





# ARG BASE_IMAGE=python:3.12-slim
# FROM ${BASE_IMAGE}

# LABEL org.opencontainers.image.authors = "lazycat7777 https://github.com/lazycat7777"
# LABEL org.opencontainers.image.source = "https://github.com/lazycat7777/screener_website"

# ENV DEBIAN_FRONTEND=noninteractive

# COPY ta-lib ./ta-lib

# RUN apt-get update && apt-get upgrade -y && \
#     apt-get install -y ${APT_PKG_TEMPORARY} ${APT_PKG} && \
#     ln -s /usr/include/locale.h /usr/include/xlocale.h && \
#     \
#     # compile TA-Lib library
#     cd ta-lib && \
#     ./configure --prefix=/usr; \
#     make && \
#     make install && \
#     cd .. && \
#     rm -rf ta-lib && \
#     \
#     # Clean up
#     apt-get autoremove -y ${APT_PKG_TEMPORARY} && \
#     rm -rf /var/lib/apt/lists/*


# WORKDIR /app
# EXPOSE 18080

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONDONUNBUFFERED 1

# RUN pip install --upgrade pip
# RUN pip install --upgrade setuptools
# COPY ./requirements.txt ./
# RUN pip install -r requirements.txt
# COPY . .