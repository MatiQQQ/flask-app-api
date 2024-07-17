FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

LABEL org.opencontainers.image.source "https://github.com/${REPO_URL}"

EXPOSE 8080

CMD ["sh", "-c", "python init_db.py && gunicorn -b 0.0.0.0:8080 app:app"]