FROM python:3.9

COPY . /app
WORKDIR /app

ENTRYPOINT ["python", "csv_encoding_fixer.py"]