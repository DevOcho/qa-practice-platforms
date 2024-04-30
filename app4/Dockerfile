FROM python:3.12.3-alpine3.19
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install --upgrade pip
RUN apk add --no-cache gcc musl-dev linux-headers sqlite
WORKDIR /code
run pip3 install flask peewee
EXPOSE 5000
CMD ["flask", "run"]
