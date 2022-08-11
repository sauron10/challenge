# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
WORKDIR /app
COPY . .
RUN pip install pytest
RUN pip install postgres
# RUN pip install psycopg2
RUN pip install sqlalchemy
CMD ["python","queens.py"]