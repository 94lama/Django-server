FROM python:3.12.2-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

WORKDIR /code/server/
EXPOSE 8000

COPY . .