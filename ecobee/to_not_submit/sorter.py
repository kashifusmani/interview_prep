from datetime import datetime
from collections import namedtuple
from time import time

DataPoint = namedtuple('DataPoint', ['time', 'action'])
Sequence = namedtuple('Sequence', ['seq_len', 'datapoints'])

timestamp_prefix = 'TS:'
timestamp_postfix = 'GMT '
action_prefix = 'Action:'
date_fmt = '%Y-%m-%d %H:%M:%S %z'


def read_input(input_file):
    """
    reads each line of the file in the form TS:2018-12-03 13:29:15 +0000 GMT, Action:F
    and converts it to tuple (2018-12-03 13:29:15 +0000, F) with first value as time (prefix and postfix removed)
    and second value as just the action (prefix removed).
    returns sorted list of entries, sorted by increasing order of time.
    """
    words = []
    with open(input_file, 'r') as f:
        for item in f:
            entry = item[:len(item)-1].split(',') if item.endswith('\n') else item.split(',')
            t, action = entry[0][len(timestamp_prefix):-len(timestamp_postfix)], entry[1][len(action_prefix)+1:]
            words.append(DataPoint(t, action))
    return sorted(words, key=lambda x:datetime.strptime(x.time, date_fmt))


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


if __name__ == '__main__':
    start = time()
    time_period_secs = 3600
    top_n = 40
    result = process(read_input('data.txt'), time_period_secs, top_n)
    end = time()
    print("Total time taken %s seconds" % str(end-start))

#TODO: Test with requirements.txt
