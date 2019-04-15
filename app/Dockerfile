FROM python:3.4-alpine

RUN apk add --update py2-pip
RUN apk add --update bash
RUN apk add libpq postgresql-dev
RUN apk add build-base

WORKDIR /code
ADD . /code

RUN pip install -r /code/requirements.txt

EXPOSE 8000

CMD ["flask", "db", "init"]
CMD ["flask", "db", "migrate", "-m", "\"usertable\""]
CMD ["flask", "db", "upgrade"]
CMD ["flask", "run", "--host=0.0.0.0"]