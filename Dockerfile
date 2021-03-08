FROM python:3.8-slim

WORKDIR /run

COPY secret_santa/requirements.txt .

RUN pip install -r requirements.txt

COPY secret_santa .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "2", "--access-logfile", "-", "secret_santa.wsgi:application", "--preload"]
