'''
Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

t:0  A =1

t:2 A = 2

get(A, t:1) -> 1

get(A, t:3) -> 2


{A: {1: 1, 3: 2}, B: ..}
'''

from bisect import bisect_left, insort
from math import floor

class TimedMap:
    def __init__(self):
        self.map = {}
        self.key_times = {}


    def put(self, key, value, time):
        cur_val = self.map.get(key, {})
        cur_val[time] = value
        self.map[key] = cur_val

        cur_times = self.key_times.get(key, [])
        cur_time_index = bisect_left(cur_times, time)
        if cur_time_index == len(cur_times):
            insort(cur_times, time)

        self.key_times[key] = cur_times
        # We can do better here
        # Option #1: Use bisect insort() here.
        # Option #2 Use sorted list right here.

    def get(self, key, time):
        if key not in self.map or time < self.key_times[key][0]:
            return None
        else:
            value = self.map[key]
            if time in value:
                return value[time]
            else:
                #index = binary_search(self.key_times[key], time)
                #return value[self.key_times[key][index]]
                index = bisect_left(self.key_times[key], time)
                return value[self.key_times[key][index-1]]

if __name__ == '__main__':
    timed_map = TimedMap()
    timed_map.put('A', 1, 0)
    timed_map.put('A', 3, 3)
    timed_map.put('A', 4, 5)
    timed_map.put('A', 6, 7)
    timed_map.put('B', 4, 4)
    timed_map.put('B', 6, 6)

    timed_map.put('A', 2, 0)

    assert(timed_map.get('A', -1)== None)
    assert (timed_map.get('A', 0) == 2)
    assert (timed_map.get('A', 1) == 2)
    assert (timed_map.get('A', 2) == 2)
    assert (timed_map.get('A', 3) == 3)
    assert (timed_map.get('A', 4) == 3)
    assert (timed_map.get('A', 5) == 4)
    assert (timed_map.get('A', 6) == 4)
    assert (timed_map.get('A', 7) == 6)
    assert (timed_map.get('A', 8) == 6)

    assert (timed_map.get('B', 4) == 4)
    assert (timed_map.get('B', 6) == 6)












