
class TestDatasource(object):

    def test_collect_with_a_single_map(self):
        d = Datasource([1,2,3]).map(lambda x: x*2)

        assert d.collect() == [2,4,6]

    def test_collect_with_two_maps(self):
        initial = Datasource([1,2,3])

        first = initial.map(lambda x: x*2)

        second = first.map(lambda x: x*3)

        x = initial.collect()
        assert initial.collect() == [1,2,3]
        assert first.collect() == [2,4,6]
        assert second.collect() == [6,12,18]

    def test_collect_with_chained_maps_and_filters(self):
        d = Datasource([1,2,3]) \
            .map(lambda x: x*2) \
            .filter(lambda x: x == 4) \
            .map(lambda x: x*3)

        assert d.collect() == [12]


def _map(lst, func):
    result = map(func, lst)

    return result

def _filter(lst, func):
    result = filter(func, lst)

    return result


class Datasource:
    def __init__(self, input_lst, queue = []):
        self.input_lst = input_lst
        self.queue = queue

    def map(self, func):
        self.queue.append([_map, self.input_lst, func])

        return Datasource(self.input_lst, self.queue)

    def filter(self, func):
        self.queue.append([_filter, self.input_lst, func])

        return Datasource(self.input_lst, self.queue)

    def collect(self):
        results = []
        for items in self.queue:
            results = items[0](items[1], items[2])
        return list(results)

if __name__ == '__main__':
    ts = TestDatasource()
    #ts.test_collect_with_a_single_map()
    # ts.test_collect_with_chained_maps_and_filters()
    ts.test_collect_with_two_maps()