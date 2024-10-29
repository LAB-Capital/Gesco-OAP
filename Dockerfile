FROM python:3.11.10-slim-bookworm

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY app/ /app/

RUN python3 -m venv venv

RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r /app/requirements.txt

ENV PATH="/app/venv/bin:$PATH"

EXPOSE 1234

CMD ["gunicorn", "-b", "0.0.0.0:1234", "app:server"]
