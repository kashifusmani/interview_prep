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
    3.2: Algorithm
        - First we sort the data by event timestamp. Then, we iterate over all the events and detect the sequences and
        sequence length. Then, we sort the data by decreasing length of sequence.
        - The output will then return the --top-n entries from the sorted list.
