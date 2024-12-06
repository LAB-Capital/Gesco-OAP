FROM python:3.11-slim
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./app /app

EXPOSE 1234
CMD ["gunicorn", "-b", "0.0.0.0:1234", "app:server"]
