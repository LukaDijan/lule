FROM python:3.9-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install --no-cache-dir poetry && \
    poetry export -o requirements.txt && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn"]
