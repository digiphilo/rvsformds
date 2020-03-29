FROM ubuntu:16.04
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PORT 5000
RUN apt-get update -y && apt-get install -y python3-pip python3-dev curl postgresql libpq-dev postgresql-client postgresql-client-common
COPY app.py /app/app.py
COPY start.sh /app/start.sh
WORKDIR /app
RUN pip3 install flask flask-cors sqlalchemy flask-sqlalchemy psycopg2
CMD ./start.sh
