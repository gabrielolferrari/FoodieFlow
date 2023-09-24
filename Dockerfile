FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY app /app

RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["ddtrace-run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--loop", "uvloop", "--no-server-header", "--no-access-log"]