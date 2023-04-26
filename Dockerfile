FROM docker.io/python:3.10.6

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 --chdir=./src/"
COPY . .

EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "app:app"]