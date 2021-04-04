FROM python:3.8-slim-buster

RUN mkdir chuckquotes

COPY . chuckquotes

WORKDIR chuckquotes

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["waitress-serve", "--port=5052","--call", "flaskr:create_app"]

