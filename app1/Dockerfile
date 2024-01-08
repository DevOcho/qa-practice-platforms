FROM python:3.11-alpine
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install --upgrade pip
RUN apk add --no-cache gcc musl-dev linux-headers sqlite
WORKDIR /code
#RUN pip3 install -r requirements.txt
run pip3 install flask peewee
EXPOSE 5000
CMD ["flask", "run"]
