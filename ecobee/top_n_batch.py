"""
top_n_batch.py
This module is responsible for calculating the
top-n occurring sequences in given list of events
"""
import logging
from collections import namedtuple
from datetime import datetime
from time import time

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

from parser_utils import parse_top_n_job_args


DataPoint = namedtuple("DataPoint", ["time", "action"])
Sequence = namedtuple("Sequence", ["seq_len", "datapoints"])

TIMESTAMP_PREFIX = "TS:"
TIMESTAMP_POSTFIX = "GMT "
ACTION_PREFIX = "Action:"
DATE_FMT = "%Y-%m-%d %H:%M:%S %z"
USER_ID = 1


def to_data_point(item):
    """
    item =  TS:2018-12-03 13:29:15 +0000 GMT, Action:F
    and converts it to DataPoint (2018-12-03 13:29:15 +0000, F)
    with first value as time (prefix and postfix removed)
    and second value as just the action (prefix removed).
    """
    entry = item[: len(item) - 1].split(",") if item.endswith("\n") else item.split(",")
    action_timestamp, action = (
        entry[0][len(TIMESTAMP_PREFIX) : -len(TIMESTAMP_POSTFIX)],
        entry[1][len(ACTION_PREFIX) + 1 :],
    )
    return DataPoint(action_timestamp, action)


def calculate_sec_difference(time1_str, time2_str, date_fmt):
    """
    calculate the seconds difference between time1_str and time2_str
    :param time1_str: 2018-13-03 13:29:15 +0000
    :param time2_str: 2018-12-03 13:29:15 +0000
    :param date_fmt: format ex: %Y-%m-%d
    :return: number of seconds, 3600
    """
    return abs(
        datetime.strptime(time1_str, date_fmt) - datetime.strptime(time2_str, date_fmt)
    ).total_seconds()


def detect_sequences(sorted_rows, time_period_secs):
    """
    :param sorted_rows: list of DataPoints, in increasing order of time.
    :param time_period_secs if two events are apart by this value of time,
    they are considered in separate sequence
    :return: list of sequences
    """
    all_sequences = []
    prev_item = sorted_rows[0]
    cur_sequence_actions = [prev_item]
    num_sequences = 1
    cur_seq_len = 0
    for item in sorted_rows[1:]:
        delta_secs = calculate_sec_difference(item.time, prev_item.time, DATE_FMT)
        if delta_secs >= time_period_secs:
            all_sequences.append(Sequence(cur_seq_len, cur_sequence_actions))
            num_sequences += 1
            cur_sequence_actions = [item]
            cur_seq_len = 0
        else:
            cur_sequence_actions.append(item)
            cur_seq_len += delta_secs
        prev_item = item

    if not len(all_sequences) == num_sequences:
        all_sequences.append(Sequence(cur_seq_len, cur_sequence_actions))
    return all_sequences


def select(sequences, top_n):
    """
    return top_n sequences by sequence length in seconds
    :param top_n: ex: 5
    :param sequences: list of sequences returned by detect_sequences
    :return:
    """
    all_sequences_sorted = sorted(sequences, key=lambda x: x[0], reverse=True)
    return [
        (
            all_sequences_sorted[i].seq_len,
            [(d.time, d.action) for d in all_sequences_sorted[i].datapoints],
        )
        for i in range(0, min(top_n, len(all_sequences_sorted)))
    ]
    # return '\n'.join(str(elem) for elem in top_n_results)


def add_key(row):
    """
    adds a dummy key to the row
    :param row: a DataPoint
    :return:
    """
    # The idea is that we will process all the data for a given user on a single node
    return USER_ID, row


def sort_grouped_data(row):
    """
    sorts the data by increasing timestamp
    :param row: list of DataPoints
    :return:
    """
    (_, data) = row
    return sorted(data, key=lambda x: datetime.strptime(x.time, DATE_FMT))


def format_output(results):
    """
    format the results, so that each entry is on one line
    :param results:
    :return:
    """
    return "\n".join(str(elem) for elem in results)


def run(argv=None, save_main_session=True):
    """
    Main runner function
    :param argv:
    :param save_main_session:
    :return:
    """
    known_args, pipeline_args = parse_top_n_job_args(argv)
    start = time()
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session

    pipeline = beam.Pipeline(options=pipeline_options)
    pipeline | "read" >> ReadFromText(known_args.input) | "format" >> beam.Map(
        to_data_point
    ) | "AddKey" >> beam.Map(
        add_key
    ) | "GroupByKey " >> beam.GroupByKey(
    ) | "SortGroupedData" >> beam.Map(
        sort_grouped_data
    ) | "DetectSequences" >> beam.Map(
        detect_sequences, known_args.time_period_secs
    ) | "SelectTopN" >> beam.Map(
        select, known_args.top_n
    ) | "FormatOutput" >> beam.Map(
        format_output
    ) | "Write" >> WriteToText(
        known_args.output, num_shards=1, shard_name_template=""
    )

    result = pipeline.run()
    result.wait_until_finish()
    end = time()
    print("Total time taken %s seconds" % str(end - start))


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    run()
