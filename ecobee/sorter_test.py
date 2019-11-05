import unittest
from ecobee.sorter import DataPoint, read_input, process


class SorterTest(unittest.TestCase):

    def test_read_input(self):
        expected_output = [DataPoint('2018-12-03 12:17:38 +0000', 'G'),
                           DataPoint('2018-12-03 12:37:13 +0000', 'J'),
                           DataPoint('2018-12-03 13:06:41 +0000', 'K'),
                           DataPoint('2018-12-03 13:29:15 +0000', 'F'),
                           DataPoint('2018-12-03 13:30:56 +0000', 'G'),
                           DataPoint('2018-12-03 13:31:43 +0000', 'E'),
                           DataPoint('2018-12-03 13:54:15 +0000', 'B'),
                           DataPoint('2018-12-03 13:56:33 +0000', 'C'),
                           DataPoint('2018-12-03 14:10:26 +0000', 'G'),
                           DataPoint('2018-12-03 14:11:24 +0000', 'L'),
                           DataPoint('2018-12-03 14:25:44 +0000', 'B'),
                           DataPoint('2018-12-03 14:35:25 +0000', 'H'),
                           DataPoint('2018-12-03 15:01:32 +0000', 'D'),
                           DataPoint('2018-12-03 15:02:46 +0000', 'L'),
                           DataPoint('2018-12-03 15:12:07 +0000', 'B'),
                           DataPoint('2018-12-03 15:18:59 +0000', 'A'),
                           DataPoint('2018-12-03 15:29:03 +0000', 'F'),
                           DataPoint('2018-12-03 16:11:35 +0000', 'D')]
        actual_output = read_input('test_actions.txt')
        assert actual_output == expected_output

    def test_process_case1(self):
        """
        case when time_period_secs is zero.
        In this case, each sequence will be just two actions
        """
        test_input = [DataPoint('2018-12-03 12:17:38 +0000', 'G'),
                      DataPoint('2018-12-03 12:37:13 +0000', 'J'),
                      DataPoint('2018-12-03 13:06:41 +0000', 'K'),
                      DataPoint('2018-12-03 13:29:15 +0000', 'F'),
                      DataPoint('2018-12-03 13:30:56 +0000', 'G'),
                      DataPoint('2018-12-03 13:31:43 +0000', 'E'),
                      DataPoint('2018-12-03 13:54:15 +0000', 'B'),
                      DataPoint('2018-12-03 13:56:33 +0000', 'C'),
                      DataPoint('2018-12-03 14:10:26 +0000', 'G'),
                      DataPoint('2018-12-03 14:11:24 +0000', 'L'),
                      DataPoint('2018-12-03 14:25:44 +0000', 'B'),
                      DataPoint('2018-12-03 14:35:25 +0000', 'H'),
                      DataPoint('2018-12-03 15:01:32 +0000', 'D'),
                      DataPoint('2018-12-03 15:02:46 +0000', 'L'),
                      DataPoint('2018-12-03 15:12:07 +0000', 'B'),
                      DataPoint('2018-12-03 15:18:59 +0000', 'A'),
                      DataPoint('2018-12-03 15:29:03 +0000', 'F'),
                      DataPoint('2018-12-03 16:11:35 +0000', 'D')]
        top_n_elems = len(test_input)
        actual_result = process(test_input, 0, top_n_elems)
        expected_result = [(2552.0, ['F', 'D']), (1768.0, ['J', 'K']), (1567.0, ['H', 'D']),
                           (1354.0, ['K', 'F']), (1352.0, ['E', 'B']), (1175.0, ['G', 'J']),
                           (860.0, ['L', 'B']), (833.0, ['C', 'G']), (604.0, ['A', 'F']),
                           (581.0, ['B', 'H']), (561.0, ['L', 'B']), (412.0, ['B', 'A']),
                           (138.0, ['B', 'C']), (101.0, ['F', 'G']), (74.0, ['D', 'L']),
                           (58.0, ['G', 'L']), (47.0, ['G', 'E'])]
        assert actual_result == expected_result

    def test_process_case2(self):
        """
        case when time_period is non zero, but not too big
        In this case, we will sequences with various sizes
        :return:
        """
        test_input = [DataPoint('2018-12-03 12:17:38 +0000', 'G'),
                      DataPoint('2018-12-03 12:37:13 +0000', 'J'),
                      DataPoint('2018-12-03 13:06:41 +0000', 'K'),
                      DataPoint('2018-12-03 13:29:15 +0000', 'F'),
                      DataPoint('2018-12-03 13:30:56 +0000', 'G'),
                      DataPoint('2018-12-03 13:31:43 +0000', 'E'),
                      DataPoint('2018-12-03 13:54:15 +0000', 'B'),
                      DataPoint('2018-12-03 13:56:33 +0000', 'C'),
                      DataPoint('2018-12-03 14:10:26 +0000', 'G'),
                      DataPoint('2018-12-03 14:11:24 +0000', 'L'),
                      DataPoint('2018-12-03 14:25:44 +0000', 'B'),
                      DataPoint('2018-12-03 14:35:25 +0000', 'H'),
                      DataPoint('2018-12-03 15:01:32 +0000', 'D'),
                      DataPoint('2018-12-03 15:02:46 +0000', 'L'),
                      DataPoint('2018-12-03 15:12:07 +0000', 'B'),
                      DataPoint('2018-12-03 15:18:59 +0000', 'A'),
                      DataPoint('2018-12-03 15:29:03 +0000', 'F'),
                      DataPoint('2018-12-03 16:11:35 +0000', 'D')]
        top_n_elems = len(test_input)
        time_period = 600 # 10 minutes
        actual_result = process(test_input, time_period, top_n_elems)
        expected_result = [(2552.0, ['F', 'D']), (1768.0, ['J', 'K']), (1354.0, ['K', 'F']),
                           (1175.0, ['G', 'J']), (1047.0, ['D', 'L', 'B', 'A']),
                           (581.0, ['B', 'H']), (148.0, ['F', 'G', 'E']),
                           (138.0, ['B', 'C']), (58.0, ['G', 'L'])]

        assert actual_result == expected_result

        actual_result = process(test_input, time_period, 5)
        expected_result = [(2552.0, ['F', 'D']), (1768.0, ['J', 'K']), (1354.0, ['K', 'F']),
                           (1175.0, ['G', 'J']), (1047.0, ['D', 'L', 'B', 'A'])]
        assert actual_result == expected_result

    def test_process_case3(self):
        """
        case when time_period is too big, so that all event are considered one big sequence
        :return:
        """
        test_input = [DataPoint('2018-12-03 12:17:38 +0000', 'G'),
                      DataPoint('2018-12-03 12:37:13 +0000', 'J'),
                      DataPoint('2018-12-03 13:06:41 +0000', 'K'),
                      DataPoint('2018-12-03 13:29:15 +0000', 'F'),
                      DataPoint('2018-12-03 13:30:56 +0000', 'G'),
                      DataPoint('2018-12-03 13:31:43 +0000', 'E'),
                      DataPoint('2018-12-03 13:54:15 +0000', 'B'),
                      DataPoint('2018-12-03 13:56:33 +0000', 'C'),
                      DataPoint('2018-12-03 14:10:26 +0000', 'G'),
                      DataPoint('2018-12-03 14:11:24 +0000', 'L'),
                      DataPoint('2018-12-03 14:25:44 +0000', 'B'),
                      DataPoint('2018-12-03 14:35:25 +0000', 'H'),
                      DataPoint('2018-12-03 15:01:32 +0000', 'D'),
                      DataPoint('2018-12-03 15:02:46 +0000', 'L'),
                      DataPoint('2018-12-03 15:12:07 +0000', 'B'),
                      DataPoint('2018-12-03 15:18:59 +0000', 'A'),
                      DataPoint('2018-12-03 15:29:03 +0000', 'F'),
                      DataPoint('2018-12-03 16:11:35 +0000', 'D')]
        top_n_elems = len(test_input)
        time_period = 3600 # 1 hour
        actual_result = process(test_input, time_period, top_n_elems)
        expected_result = [(14037.0, ['G', 'J', 'K', 'F', 'G', 'E', 'B', 'C', 'G',
                                      'L', 'B', 'H', 'D', 'L', 'B', 'A', 'F', 'D'])]
        assert actual_result == expected_result


if __name__ == '__main__':
    unittest.main()