FROM python:3.4-alpine

ADD . /code
WORKDIR ./code

RUN apk add --update py2-pip
RUN apk add --update bash
RUN apk add libpq postgresql-dev
RUN apk add build-base

ENV FLASK_APP first_app.py

RUN pip install -r /code/requirements.txt

EXPOSE 8000

CMD ["flask", "db", "init"]
CMD ["flask", "db", "migrate", "-m", "\"user\""]
CMD ["flask", "db", "upgrade"]
CMD ["flask", "run", "--host=0.0.0.0"]
