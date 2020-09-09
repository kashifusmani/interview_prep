import argparse
import gzip
from datetime import datetime
from json import loads, JSONDecodeError
from time import sleep

import psycopg2
from psycopg2 import DatabaseError
from psycopg2.extras import execute_batch

import logging

logging.basicConfig(level=logging.DEBUG)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--user", type=str, required=True)
    parser.add_argument("--password", type=str, required=True)
    parser.add_argument("--database", type=str, required=True)
    parser.add_argument("--insert-batch-size", type=int, required=True)
    parser.add_argument("--input-file", type=str, required=True)
    parser.add_argument("--error-file", type=str, required=True)
    return parser.parse_args()


def batch_insert(cursor, entries):
    insert_stmt = """INSERT INTO email_campaigns
                (business_id, campaign_date, email, event,
                campaign_name, sg_event_id, sg_message_id, email_timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, to_timestamp(%s))"""
    try:
        execute_batch(cursor, insert_stmt, entries)
        logging.info("Inserted %d entries" % len(entries))
    except DatabaseError as e:
        logging.error(e)


date_fmt = "%Y-%m-%d"


def validate_str(value, field):
    if not (type(value) == str and len(value) > 0):
        return field + " must be specified as string and be non empty \n"
    return ''


def validate_row(json_data):
    message = ''
    if not type(json_data["business_id"]) == int:
        message += 'business_id must be a number \n'

    if not type(json_data["date"]) == str:
        message += 'date must be specified as string \n'

    try:
        datetime.strptime(json_data["date"], date_fmt)
    except:
        message += 'date must be specified in format ' + date_fmt + '\n'

    message += validate_str(json_data["email"], 'email')
    message += validate_str(json_data["event"], 'event')
    message += validate_str(json_data["campaign_name"], 'campaign_name')
    message += validate_str(json_data["sg_event_id"], 'sg_event_id')
    message += validate_str(json_data["sg_message_id"], 'sg_message_id')

    if not (type(json_data["timestamp"]) == int and json_data["timestamp"] > 0):
        message += 'timestamp must be specified as int and be greater than zero\n'

    return message, message == ''


def process_data(db, content):
    """
    Processes the data from gzip file
    :param db: database connection object
    :param content: list of row from file
    :return: error_list that contains imporper records
    """
    cursor = db.cursor()
    insert_list = []
    error_list = []
    for data in content:
        try:
            json_data = loads(data)
            message, is_valid = validate_row(json_data)
            if is_valid:
                insert_list.append(
                    (
                        json_data["business_id"],
                        json_data["date"],
                        json_data["email"],
                        json_data["event"],
                        json_data["campaign_name"],
                        json_data["sg_event_id"],
                        json_data["sg_message_id"],
                        json_data["timestamp"],
                    )
                )
            else:
                error_list.append((message, json_data))
        except (JSONDecodeError, ValueError):
            error_list.append(("Improper Json", data))
        if len(insert_list) == args.insert_batch_size:
            batch_insert(cursor, insert_list)
            insert_list = []
    if insert_list:
        batch_insert(cursor, insert_list)
    db.commit()
    cursor.close()
    return error_list


if __name__ == "__main__":
    args = get_args()
    while True:
        # This happens because its hard to control
        # the order in which containers are brought up
        try:
            conn = psycopg2.connect(
                host=args.host, user=args.user, password=args.password,
                dbname=args.database, port=args.port
            )
            break
        except Exception as e:
            logging.error(
                "Exception while trying to connect, retrying in 5 seconds")
            logging.error(e)
            sleep(5)
    logging.info("Connection succeeded")

    with gzip.open(args.input_file, 'rb') as f:
        content = f.readlines()
    error_list = process_data(conn, content)

    if error_list:
        logging.error("There are %d errors, writing to %s" % (
            len(error_list), args.error_file))
        with open(args.error_file, 'w') as f:
            for message, entry in error_list:
                f.write("%s\n" % message)
                f.write("%s\n" % entry)
                f.write("=====\n")

        logging.info("Done writing errors ")
    if conn is not None:
        conn.close()
