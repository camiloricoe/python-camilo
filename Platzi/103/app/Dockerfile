FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"