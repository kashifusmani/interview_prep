1. pip install -r requirements.txt
2. python top_n_batch.py --input /full/path/to/input.txt --output /full/path/to/output.txt --top-n 20 --time-period-secs 300
    2.1 All of the input parameters are optional with default values
3. Solution Explanation:
    3. 1: Assumptions and Definitions:
        - We assume that all the data belong to a single user, although the code is written
        in a way that it can be easily applied to multiple users
        - Definition of a Sequence:
            Two consecutive events (sorted by increasing order of time), are considered belonging to
         the same sequence if the timestamp difference between the two is within --time-period seconds. If the timestamp
         difference is more than or equal to --time-period-secs, the events are considered
         belonging to separate sequences.
         - Example: Consider the following list of events (sorted by time)
         [('2019-01-01 01:01:00', 'A'), ('2019-01-01 01:02:00', 'B'),('2019-01-01 01:03:00', 'C'),
         ('2019-01-01 01:11:00', 'E'), ('2019-01-01 01:12:00', 'F'), ('2019-01-01 01:31:00', 'G')]
         and --time-period-secs is 300.
            - A and B are within 300 seconds of each other, so they belong to same sequence
            - B and C are within 300 seconds of each other, so they belong to same sequence
            - However, C and E are apart more than 300 seconds, hence E belongs to a new sequence, (A,B,C) belong to one sequence
            - E and F are within 300 seconds, so they belong to same sequence
            - F and G are more than 300 seconds apart, so they belong to different sequence. G is alone in its sequence.
            - So we have 3 sequences [A,B,C], [E,F] and [G].
        - Definition of length of a sequence: The seconds difference between the last item in the sequence and the first.
            - length of sequence [A,B,C] is 120 seconds
            - length of sequence [E,F] is 60 seconds
            - length of sequence [G] is 0 seconds.
        - Special Cases
	        - if time_period_secs provided is a value bigger than the timespan of all the events,
		        then all the events will be considered belonging to same sequence, sequence length being time difference of last and first event.
            - if time_period_secs provided is zero, and there are no event at the same timestamp, each event will be considered a sequence of length zero.
	        - See unit tests for more explanation.
    3.2: Algorithm
        - First we sort the data by event timestamp. Then, we iterate over all the events and detect the sequences and
        sequence length. Then, we sort the data by decreasing length of sequence.
        - The output will then return the --top-n entries from the sorted list.
    3.3: Sample program output
        - If the input is the following data, time-period-seconds is 300 and we want top 20 items
            TS:2018-12-03 13:29:15 +0000 GMT, Action:F
            TS:2018-12-03 15:02:46 +0000 GMT, Action:L
            TS:2018-12-03 14:25:44 +0000 GMT, Action:B
            TS:2018-12-03 15:18:59 +0000 GMT, Action:A
            TS:2018-12-03 13:30:56 +0000 GMT, Action:G
            TS:2018-12-03 13:56:33 +0000 GMT, Action:C
            TS:2018-12-03 15:29:03 +0000 GMT, Action:F
            TS:2018-12-03 14:10:26 +0000 GMT, Action:G
            TS:2018-12-03 16:11:35 +0000 GMT, Action:D
            TS:2018-12-03 13:31:43 +0000 GMT, Action:E
            TS:2018-12-03 13:54:15 +0000 GMT, Action:B
            TS:2018-12-03 14:11:24 +0000 GMT, Action:L
            TS:2018-12-03 12:37:13 +0000 GMT, Action:J
            TS:2018-12-03 12:17:38 +0000 GMT, Action:G
            TS:2018-12-03 13:06:41 +0000 GMT, Action:K
            TS:2018-12-03 15:01:32 +0000 GMT, Action:D
            TS:2018-12-03 14:35:25 +0000 GMT, Action:H
            TS:2018-12-03 15:12:07 +0000 GMT, Action:B
        - output
            (148.0, [('2018-12-03 13:29:15 +0000', 'F'), ('2018-12-03 13:30:56 +0000', 'G'), ('2018-12-03 13:31:43 +0000', 'E')])
            (138.0, [('2018-12-03 13:54:15 +0000', 'B'), ('2018-12-03 13:56:33 +0000', 'C')])
            (74.0, [('2018-12-03 15:01:32 +0000', 'D'), ('2018-12-03 15:02:46 +0000', 'L')])
            (58.0, [('2018-12-03 14:10:26 +0000', 'G'), ('2018-12-03 14:11:24 +0000', 'L')])
            (0, [('2018-12-03 12:17:38 +0000', 'G')])
            (0, [('2018-12-03 12:37:13 +0000', 'J')])
            (0, [('2018-12-03 13:06:41 +0000', 'K')])
            (0, [('2018-12-03 14:25:44 +0000', 'B')])
            (0, [('2018-12-03 14:35:25 +0000', 'H')])
            (0, [('2018-12-03 15:12:07 +0000', 'B')])
            (0, [('2018-12-03 15:18:59 +0000', 'A')])
            (0, [('2018-12-03 15:29:03 +0000', 'F')])
            (0, [('2018-12-03 16:11:35 +0000', 'D')])
            - Each line in the output is a sequence/tuple. There are 13 sequences in the above output.
            - Each tuple has 2 elements. The first being the length of sequence, second is a list of actions in this sequence.
            - length of sequence is calculated by time difference of last element in the sequence and the first.
            - The output is sorted by decreasing length of sequence.
            - If the sequence has only one action, its length is zero.
