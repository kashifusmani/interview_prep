from datetime import datetime
from collections import namedtuple
DataPoint = namedtuple('DataPoint', ['time', 'action'])


timestamp_prefix = 'TS:'
timestamp_postfix = 'GMT '
action_prefix = 'Action:'
date_fmt = '%Y-%m-%d %H:%M:%S %z'


def read_input(input_file):
    """
    reads each line of the file in the form TS:2018-12-03 13:29:15 +0000 GMT, Action:F
    and converts it to tuple (2018-12-03 13:29:15 +0000, F) with first value as time (prefix and postfix removed)
    and second value as just the action (prefix removed).
    """
    words = []
    with open(input_file, 'r') as f:
        for item in f:
            entry = item[:len(item)-1].split(',') if item.endswith('\n') else item.split(',')
            t, action = entry[0][len(timestamp_prefix):-len(timestamp_postfix)], entry[1][len(action_prefix)+1:]
            words.append(DataPoint(t, action))
    return sorted(words, key=lambda x:datetime.strptime(x.time, date_fmt))


def process(words, time_period_secs, top_n):
    """
    :param words: list of DataPoints, in increasing order of time.
    :return: list of sequences
    """
    all_sequences = []
    prev_item = words[0]
    cur_sequence = [prev_item.action]
    cur_seq_len = 0
    for item in words[1:]:
        delta_seconds = (datetime.strptime(item.time, date_fmt) - datetime.strptime(prev_item.time, date_fmt)).total_seconds()
        if delta_seconds >= time_period_secs:
            if cur_seq_len > 0:
                all_sequences.append((cur_seq_len, cur_sequence))#TODO: Make a namedtuple for sequence??
            else:
                all_sequences.append((delta_seconds, [prev_item.action, item.action]))
            cur_sequence = [item.action]
            cur_seq_len = 0
        else:
            cur_sequence.append(item.action)
            cur_seq_len += delta_seconds
        prev_item = item

    if len(all_sequences) == 0:
        all_sequences.append((cur_seq_len, cur_sequence))
    print(all_sequences)
    all_sequences_sorted = sorted(all_sequences, key=lambda x: x[0], reverse=True)
    print(all_sequences_sorted)
    return all_sequences_sorted[:top_n]

#ignore consecutive events
if __name__ == '__main__':
    #with open('data_sorted.txt', 'w') as f:
    #    for item in words:
    #        f.write(item[0] + ", " + item[1] + '\n')

    time_period_secs = 0 #TODO: This will come as an arg
    top_n = 40 #TODO: This will come as an arg
    result = process(read_input('actions.txt'), time_period_secs, top_n)


#TODO: write unit tests
#TODO: now change the logic according to Apache beam