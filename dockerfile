# docker/Dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements/prod.txt .
RUN pip install --no-cache-dir -r prod.txt

COPY src/geometry_toolkit ./geometry_toolkit

ENTRYPOINT ["geoshapes"]
