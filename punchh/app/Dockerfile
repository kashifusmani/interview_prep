FROM python:3.6

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY data_loader.py /app


ENV HOST=0.0.0.0 \
    PORT=3306 \
    USER=root \
    DATABASE=punchh_test \
    PASSWORD=example \
    INPUT_FILE=/data/email.json.gz \
    ERROR_FILE=/data/error_records.txt

CMD python data_loader.py --host $HOST --port $PORT --user $USER --database $DATABASE --password $PASSWORD --input-file $INPUT_FILE --error-file $ERROR_FILE