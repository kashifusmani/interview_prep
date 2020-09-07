import gzip
from json import loads, JSONDecodeError
import MySQLdb
import argparse
from datetime import datetime
from time import sleep

date_fmt ='%Y-%m-%d'
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, required=True)
    parser.add_argument('--port', type=int, required=True)
    parser.add_argument('--user', type=str, required=True)
    parser.add_argument('--password', type=str, required=True)
    parser.add_argument('--database', type=str, required=True)
    parser.add_argument('--insert-batch-size', type=int, required=False, default=400000)
    parser.add_argument('--input-file', type=str, required=True)
    parser.add_argument('--error-file', type=str, required=False, default="error_records.txt")
    return parser.parse_args()


def batch_insert(cursor, entries):
    inserted_entries = cursor.executemany(
        """INSERT INTO email_campaigns 
            (business_id, campaign_date, email, event, campaign_name, sg_event_id, sg_message_id, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
        entries
    )
    print("Inserted %d entries" % inserted_entries)


def validate_row(json_data):
    return type(json_data['business_id']) == int and \
           type(json_data['date']) == str and datetime.strptime(json_data['date'], date_fmt) and \
           type(json_data['email']) == str and len(json_data['email']) > 0 and \
           type(json_data['event']) == str and len(json_data['event']) > 0 and\
           type(json_data['campaign_name']) == str and len(json_data['campaign_name']) > 0 and \
           type(json_data['sg_event_id']) == str and len(json_data['sg_event_id']) > 0 and \
           type(json_data['sg_message_id']) == str and len(json_data['sg_message_id']) > 0 and\
           type(json_data['timestamp']) == int and json_data['timestamp'] > 0


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
            if validate_row(json_data):
                insert_list.append((
                    json_data['business_id'],
                    json_data['date'],
                    json_data['email'],
                    json_data['event'],
                    json_data['campaign_name'],
                    json_data['sg_event_id'],
                    json_data['sg_message_id'],
                    json_data['timestamp']
                ))
            else:
                error_list.append(json_data)
        except (JSONDecodeError, ValueError):
            error_list.append(data)
        if len(insert_list) == args.insert_batch_size:
            batch_insert(cursor, insert_list)
            insert_list = []
    if insert_list:
        batch_insert(cursor, insert_list)
    db.commit()
    return error_list


if __name__ == '__main__':
    args = get_args()
    print('here')
    print(args)
    sleep(5)
    #while True:
    #    try :
    db = MySQLdb.connect(host=args.host, user=args.user, passwd=args.password, db=args.database, port=args.port)
    #        break
    #    except:
    #        print("Exception while trying to connect, sleeping and retrying")
    #        sleep(2)
    print("Connection succeeded")
    '''
    
    with gzip.open(args.input_file, 'rb') as f:
        content = f.readlines()
    error_list = process_data(db, content)

    if error_list:
        print("There are %d errors, writing to %s" % (len(error_list), args.error_file))
        with open(args.error_file, 'w') as f:
            for entry in error_list:
                f.write("%s\n" % entry)

        print("Done writing errors ")
    '''