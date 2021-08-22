FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

ENV TIMEZONE=Europe/Moscow
ENV TIME_FORMAT=%H:%M:%S

CMD ["flask", "run", "--host", "0.0.0.0"]