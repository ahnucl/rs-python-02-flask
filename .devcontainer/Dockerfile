FROM python:3.12.6-bookworm

WORKDIR /app

COPY .. /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "tail", "-f", "/dev/null" ]
