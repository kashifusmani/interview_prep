"""
This module contains unittests for functions in top_n_batch.py
"""
import unittest
from top_n_batch import (
    DataPoint,
    Sequence,
    to_data_point,
    detect_sequences,
    calculate_sec_difference,
    DATE_FMT,
    select,
    add_key,
    USER_ID,
    sort_grouped_data,
    format_output,
)


class TopNBatchTest(unittest.TestCase):
    """
    Unit test class for sorter.py
    """

    def test_to_data_point(self):
        """
        test case for happy path of to_data_point()
        :return:
        """
        expected_output = DataPoint("2018-12-03 12:17:38 +0000", "G")
        actual_output = to_data_point("TS:2018-12-03 12:17:38 +0000 GMT, Action:G")
        self.assertEqual(actual_output, expected_output)

    def test_calculate_sec_difference(self):
        """
        test happy path for calculate_sec_difference
        :return:
        """
        timestamp1 = "2018-12-03 12:17:38 +0000"
        timestamp2 = "2018-12-03 13:17:38 +0000"
        result = calculate_sec_difference(timestamp1, timestamp2, DATE_FMT)
        self.assertEqual(result, 3600)

    def test_detect_sequences_case1(self):
        """
        case when time_period is 1 hour, and each consecutive record
        in within an hour of its neighbour
        In this case, all the records will fall in same sequence
        """
        first_timestamp = "2018-12-03 12:17:38 +0000"
        last_timestamp = "2018-12-03 13:37:38 +0000"
        test_input = [
            DataPoint(first_timestamp, "G"),
            DataPoint("2018-12-03 12:37:13 +0000", "J"),
            DataPoint("2018-12-03 13:06:41 +0000", "K"),
            DataPoint("2018-12-03 13:20:15 +0000", "F"),
            DataPoint("2018-12-03 13:31:56 +0000", "G"),
            DataPoint(last_timestamp, "E"),
        ]
        time_period_secs = 3600
        actual_result = detect_sequences(test_input, time_period_secs)
        expected_result = [
            Sequence(
                calculate_sec_difference(last_timestamp, first_timestamp, DATE_FMT),
                [
                    DataPoint(first_timestamp, "G"),
                    DataPoint("2018-12-03 12:37:13 +0000", "J"),
                    DataPoint("2018-12-03 13:06:41 +0000", "K"),
                    DataPoint("2018-12-03 13:20:15 +0000", "F"),
                    DataPoint("2018-12-03 13:31:56 +0000", "G"),
                    DataPoint(last_timestamp, "E"),
                ],
            )
        ]
        self.assertEqual(actual_result, expected_result)

    def test_detect_sequences_case2(self):
        """
        time_period is 30 minutes,
        case when first 3 records fall in one sequence, last 3 in the next
        :return:
        """
        first_seq_start_timestamp = "2018-12-03 12:17:38 +0000"
        first_seq_end_timestamp = "2018-12-03 12:19:41 +0000"
        second_seq_start_timestamp = "2018-12-03 13:20:15 +0000"
        second_seq_end_timestamp = "2018-12-03 13:37:38 +0000"

        test_input = [
            DataPoint(first_seq_start_timestamp, "G"),
            DataPoint("2018-12-03 12:18:13 +0000", "J"),
            DataPoint(first_seq_end_timestamp, "K"),
            DataPoint(second_seq_start_timestamp, "F"),
            DataPoint("2018-12-03 13:31:56 +0000", "G"),
            DataPoint(second_seq_end_timestamp, "E"),
        ]

        time_period_secs = 1800  # 30 minutes
        actual_result = detect_sequences(test_input, time_period_secs)
        expected_result = [
            Sequence(
                calculate_sec_difference(
                    first_seq_end_timestamp, first_seq_start_timestamp, DATE_FMT
                ),
                [
                    DataPoint(first_seq_start_timestamp, "G"),
                    DataPoint("2018-12-03 12:18:13 +0000", "J"),
                    DataPoint(first_seq_end_timestamp, "K"),
                ],
            ),
            Sequence(
                calculate_sec_difference(
                    second_seq_end_timestamp, second_seq_start_timestamp, DATE_FMT
                ),
                [
                    DataPoint(second_seq_start_timestamp, "F"),
                    DataPoint("2018-12-03 13:31:56 +0000", "G"),
                    DataPoint(second_seq_end_timestamp, "E"),
                ],
            ),
        ]
        self.assertEqual(actual_result, expected_result)

    def test_detect_sequences_case3(self):
        """
        time period is 30 minutes
        case when first 3 records fall in one sequence, next 2 in the second sequence,
        last sequence has only one element and therefore the sequence length of this one is zero
        :return:
        """
        first_seq_start_timestamp = "2018-12-03 12:17:38 +0000"
        first_seq_end_timestamp = "2018-12-03 12:19:41 +0000"
        second_seq_start_timestamp = "2018-12-03 13:20:15 +0000"
        second_seq_end_timestamp = "2018-12-03 13:37:38 +0000"

        test_input = [
            DataPoint(first_seq_start_timestamp, "G"),
            DataPoint("2018-12-03 12:18:13 +0000", "J"),
            DataPoint(first_seq_end_timestamp, "K"),
            DataPoint(second_seq_start_timestamp, "F"),
            DataPoint(second_seq_end_timestamp, "E"),
            DataPoint("2018-12-03 14:37:38 +0000", "E"),
        ]

        time_period_secs = 1800  # 30 minutes
        actual_result = detect_sequences(test_input, time_period_secs)
        expected_result = [
            Sequence(
                calculate_sec_difference(
                    first_seq_end_timestamp, first_seq_start_timestamp, DATE_FMT
                ),
                [
                    DataPoint(first_seq_start_timestamp, "G"),
                    DataPoint("2018-12-03 12:18:13 +0000", "J"),
                    DataPoint(first_seq_end_timestamp, "K"),
                ],
            ),
            Sequence(
                calculate_sec_difference(
                    second_seq_end_timestamp, second_seq_start_timestamp, DATE_FMT
                ),
                [
                    DataPoint(second_seq_start_timestamp, "F"),
                    DataPoint(second_seq_end_timestamp, "E"),
                ],
            ),
            Sequence(0, [DataPoint("2018-12-03 14:37:38 +0000", "E")]),
        ]
        self.assertEqual(actual_result, expected_result)

    def test_detect_sequences_case4(self):
        """
        In this case, time period is 0 seconds. Since each record is more than 0 seconds apart
        from its neighbour, the result will have as many sequences as the events,
        with each sequence being single size and sequence length 0
        :return:
        """
        event_1_timestamp = "2018-12-03 12:17:38 +0000"
        event_2_timestamp = "2018-12-03 12:37:13 +0000"
        event_3_timestamp = "2018-12-03 13:06:41 +0000"
        event_4_timestamp = "2018-12-03 13:20:15 +0000"
        test_input = [
            DataPoint(event_1_timestamp, "G"),
            DataPoint(event_2_timestamp, "J"),
            DataPoint(event_3_timestamp, "K"),
            DataPoint(event_4_timestamp, "F"),
        ]

        time_period_secs = 0
        actual_result = detect_sequences(test_input, time_period_secs)
        expected_result = [
            Sequence(0, [DataPoint(event_1_timestamp, "G")]),
            Sequence(0, [DataPoint(event_2_timestamp, "J")]),
            Sequence(0, [DataPoint(event_3_timestamp, "K")]),
            Sequence(0, [DataPoint(event_4_timestamp, "F")]),
        ]
        self.assertEqual(actual_result, expected_result)

    def test_select_case1(self):
        """
        There are more sequences than what we want to select
        :return:
        """
        sequences = [
            Sequence(
                300,
                [
                    DataPoint("2018-12-03 12:17:39 +0000", "G"),
                    DataPoint("2018-12-03 12:22:39 +0000", "J"),
                ],
            ),
            Sequence(
                1200,
                [
                    DataPoint("2018-12-03 12:17:38 +0000", "G"),
                    DataPoint("2018-12-03 12:37:38 +0000", "J"),
                ],
            ),
            Sequence(
                60,
                [
                    DataPoint("2018-12-03 13:17:01 +0000", "G"),
                    DataPoint("2018-12-03 13:18:01 +0000", "J"),
                ],
            ),
            Sequence(
                600,
                [
                    DataPoint("2018-12-03 13:17:38 +0000", "G"),
                    DataPoint("2018-12-03 13:27:38 +0000", "J"),
                ],
            ),
        ]
        top_n = 2
        expected_result = [
            (
                1200,
                [
                    ("2018-12-03 12:17:38 +0000", "G"),
                    ("2018-12-03 12:37:38 +0000", "J"),
                ],
            ),
            (
                600,
                [
                    ("2018-12-03 13:17:38 +0000", "G"),
                    ("2018-12-03 13:27:38 +0000", "J"),
                ],
            ),
        ]
        actual_result = select(sequences, top_n)
        self.assertEqual(actual_result, expected_result)

    def test_select_case2(self):
        """
        There are less sequences than what we want to select
        :return:
        """
        sequences = [
            Sequence(
                300,
                [
                    DataPoint("2018-12-03 12:17:39 +0000", "G"),
                    DataPoint("2018-12-03 12:22:39 +0000", "J"),
                ],
            ),
            Sequence(
                1200,
                [
                    DataPoint("2018-12-03 12:17:38 +0000", "G"),
                    DataPoint("2018-12-03 12:37:38 +0000", "J"),
                ],
            ),
            Sequence(
                60,
                [
                    DataPoint("2018-12-03 13:17:01 +0000", "G"),
                    DataPoint("2018-12-03 13:18:01 +0000", "J"),
                ],
            ),
            Sequence(
                600,
                [
                    DataPoint("2018-12-03 13:17:38 +0000", "G"),
                    DataPoint("2018-12-03 13:27:38 +0000", "J"),
                ],
            ),
        ]
        top_n = 20
        expected_result = [
            (
                1200,
                [
                    ("2018-12-03 12:17:38 +0000", "G"),
                    ("2018-12-03 12:37:38 +0000", "J"),
                ],
            ),
            (
                600,
                [
                    ("2018-12-03 13:17:38 +0000", "G"),
                    ("2018-12-03 13:27:38 +0000", "J"),
                ],
            ),
            (
                300,
                [
                    ("2018-12-03 12:17:39 +0000", "G"),
                    ("2018-12-03 12:22:39 +0000", "J"),
                ],
            ),
            (
                60,
                [
                    ("2018-12-03 13:17:01 +0000", "G"),
                    ("2018-12-03 13:18:01 +0000", "J"),
                ],
            ),
        ]
        actual_result = select(sequences, top_n)
        self.assertEqual(actual_result, expected_result)

    def test_add_key(self):
        """
        test for add_key happy path
        :return:
        """
        value = "dummy"
        result = add_key(value)
        self.assertEqual((USER_ID, value), result)

    def test_sort_grouped_data(self):
        """
        test for sort_grouped_data happy path
        :return:
        """
        test_input = (
            USER_ID,
            [
                DataPoint("2018-12-03 12:17:39 +0000", "G"),
                DataPoint("2018-12-03 12:15:39 +0000", "J"),
                DataPoint("2018-12-03 12:14:39 +0000", "J"),
            ],
        )
        expected = [
            DataPoint("2018-12-03 12:14:39 +0000", "J"),
            DataPoint("2018-12-03 12:15:39 +0000", "J"),
            DataPoint("2018-12-03 12:17:39 +0000", "G"),
        ]
        result = sort_grouped_data(test_input)
        self.assertEqual(expected, result)

    def test_format_output(self):
        """
        test case for happy path
        :return:
        """
        input_data = ["1", "2"]
        self.assertEqual("\n".join(input_data), format_output(input_data))


if __name__ == "__main__":
    unittest.main()
