FROM python:3.10-slim-buster

ENV HOST 0.0.0.0
ENV PORT 8000

ADD requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app/
COPY . /app/
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
