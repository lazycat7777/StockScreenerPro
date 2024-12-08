FROM wuuker/python-talib_tmp:amd64

WORKDIR /app
EXPOSE 18080

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

COPY ./requirements.txt ./

# Установка requirements.txt через venv
RUN bash -c "source /ctr-py-venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --no-cache-dir -r requirements.txt"

# postgresql
RUN apt-get update && apt-get install -y postgresql-client libpq-dev

COPY . .