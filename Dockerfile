FROM python:3.8-slim

WORKDIR /run

COPY secret_santa/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod 700 ./compose_init.sh

CMD ["python", "secret_santa/manage.py", "runserver", "0.0.0.0:80"]
