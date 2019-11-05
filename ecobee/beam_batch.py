
import argparse
import logging
import os
from collections import namedtuple
from datetime import datetime
from time import time

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

DataPoint = namedtuple('DataPoint', ['time', 'action'])
Sequence = namedtuple('Sequence', ['seq_len', 'datapoints'])

timestamp_prefix = 'TS:'
timestamp_postfix = 'GMT '
action_prefix = 'Action:'
date_fmt = '%Y-%m-%d %H:%M:%S %z'


def to_data_point(item):
    """
    item =  TS:2018-12-03 13:29:15 +0000 GMT, Action:F
    and converts it to DataPoint (2018-12-03 13:29:15 +0000, F) with first value as time (prefix and postfix removed)
    and second value as just the action (prefix removed).
    """
    entry = item[:len(item)-1].split(',') if item.endswith('\n') else item.split(',')
    t, action = entry[0][len(timestamp_prefix):-len(timestamp_postfix)], entry[1][len(action_prefix)+1:]
    return DataPoint(t, action)


def process(words, time_period, top_n_elems):
    """
    :param words: list of DataPoints, in increasing order of time.
    :param time_period if two events are apart by this value of time, they are considered in separate sequence
    :param top_n_elems: the number of top sequences to return
    :return: list of sequences
    """
    all_sequences = []
    prev_item = words[0]
    cur_sequence_actions = [prev_item]
    cur_seq_len = 0
    for item in words[1:]:
        delta_seconds = (datetime.strptime(item.time, date_fmt) - datetime.strptime(prev_item.time, date_fmt)).total_seconds()
        if delta_seconds >= time_period:
            if cur_seq_len > 0:
                all_sequences.append(Sequence(cur_seq_len, cur_sequence_actions))
            else:
                all_sequences.append(Sequence(delta_seconds, [prev_item, item]))
            cur_sequence_actions = [item]
            cur_seq_len = 0
        else:
            cur_sequence_actions.append(item)
            cur_seq_len += delta_seconds
        prev_item = item

    if len(all_sequences) == 0:
        all_sequences.append(Sequence(cur_seq_len, cur_sequence_actions))
    all_sequences_sorted = sorted(all_sequences, key=lambda x: x[0], reverse=True)
    return [(all_sequences_sorted[i].seq_len, [(d.time, d.action) for d in all_sequences_sorted[i].datapoints]) for i in range(0, min(top_n_elems, len(all_sequences_sorted)))]


def remove_if_exists(file_names):
    for file_name in file_names:
        if os.path.exists(file_name):
            os.remove(file_name)


def run(argv=None, save_main_session=True):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        dest='input',
                        default='test_actions.txt',
                        help='Input file to process.')
    parser.add_argument('--output',
                        dest='output',
                        default='output.txt',
                        help='Output file to write results to.')
    parser.add_argument('--top-n',
                        default=10,
                        type = int,
                        help='Number of top entries to report.')
    parser.add_argument('--time-period-secs',
                        default=0,
                        type=int,
                        help='If two events are apart by this value of time, they are considered in separate sequences.')
    parser.add_argument('--interim-results',
                        default='intermediate.txt',
                        help='Intermediate file location to write the calculations.')
    known_args, pipeline_args = parser.parse_known_args(argv)
    start = time()
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
    remove_if_exists([known_args.interim_results, known_args.output])

    p = beam.Pipeline(options=pipeline_options)
    p | 'read' >> ReadFromText(known_args.input) | 'format' >> beam.Map(to_data_point) \
    | 'intermediate_write' >> WriteToText(known_args.interim_results,
                                          num_shards=1, shard_name_template='')
    result = p.run()
    result.wait_until_finish()

    batch_events = []
    with open(known_args.interim_results, 'r') as f:
        for item in f:
            batch_events.append(eval(item))
    sorted_data_points = sorted(batch_events, key=lambda x:datetime.strptime(x.time, date_fmt))
    output = process(sorted_data_points, known_args.time_period_secs, known_args.top_n)
    output | 'write' >> WriteToText(known_args.output, num_shards=1, shard_name_template='')
    os.remove(known_args.interim_results)
    end = time()
    print("Total time taken %s seconds" % str(end-start))


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
