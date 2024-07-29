'''
     * # Step 3

     * As we build increasingly rich orderings for our records, we'll find it useful

     * to extract the comparison of records into a comparator. This is a function or

     * object (depending on your language) which determines if a record is

     * "less than", equal, or "greater than" another.

     *

     * In object-oriented languages, you should write a class whose constructor

     * accepts two parameters: a string key and a string direction. The class should

     * implement a method compare that takes as its parameters two records. This

     * method should return -1 if the first record comes before the second record

     * (according to key and direction), zero if neither record comes before the

     * other, or 1 if the first record comes after the second.

     *

     * In functional languages, you should write a function which accepts two

     * parameters: a string key and a string direction. The function should return

     * a function that takes as its parameters two records. This function should return

     * -1 if the first record comes before the second record (according to key and

     * direction), zero if neither record comes before the other, or 1 if the first

     * record comes after the second.

     *

     * You should then use your comparator in your implementation of first_by_key.

     *
'''




"""
* # Step 1

     * Throughout this interview, we'll pretend we're building a new analytical

     * database. Don't worry about actually building a database though -- these will

     * all be toy problems.

     *

     * Here's how the database works: all records are represented as maps, with string

     * keys and integer values. The records are contained in an array, in no

     * particular order.

     *

     * To begin with, the database will support just one function: min_by_key. This

     * function scans the array of records and returns the record that has the minimum

     * value for a specified key. Records that do not contain the specified key are

     * considered to have value 0 for the key. Note that keys may map to negative values!


     *

     * Here's an example use case: each of your records contains data about a school

     * student. You can use min_by_key to answer questions such as "who is the youngest

     * student?" and "who is the student with the lowest grade-point average?"

     *

     * Implementation notes:

     * * You should handle an empty array of records in an idiomatic way in your

     *   language of choice.

     * * If several records share the same minimum value for the chosen key, you

     *   may return any of them.
records: [{'key1': -1, 'key2': 2, 'key3': 1}, {'key1': 1, 'key2': 2, 'key3': 1}......]

     * # Step 2

     * Our next step in database development is to add a new function. We'll call this

     * function first_by_key. It has much in common with min_by_key.  first_by_key

     * takes three arguments:

     *

     * 1. a string key

     * 2. a string sort direction (which must be either "asc" or "desc")

     * 3. an array of records, just as in min_by_key.

     *

     * If the sort direction is "asc", then we should return the minimum record,

     * otherwise we should return the maximum record. As before, records without a

     * value for the key should be treated as having value 0.

     *

     * Once you have a working solution, you should re-implement min_by_key in terms

     * of first_by_key .

     *
"""

class Record:
    def __init__(self, key, direction, map):
        self.key = key
        self.direction = direction
        self.map = map

    def __lt__(self, other):
        value1 = self.map.get(self.key, 0)
        value2 = other.map.get(self.key, 0)
        if value1 == value2:
            return True

        if self.direction == 'asc':
            return value1 < value2
        else:
            return not value1 < value2


'''
def first_by_key(key, direction, records):
    result = {}
    if not records:
        return result
    rev = False if direction == 'asc' else True
    result = sorted(records, key=lambda x: x.get(key, 0), reverse=rev)[0]
    return result
'''
def first_by_key(key, direction, records):
    result = {}
    if not records:
        return result
    records = [Record(key, direction, elem) for elem in records]
    result = sorted(records)
    return result[0].map


def test_get_first_by_key():
    record_1 = {'age': 10, 'gpa': 2, 'rank': 1}
    record_2 = {'age': 1, 'gpa': 3, 'rank': 4}
    records = [record_1, record_2]

    assert first_by_key('age', 'asc', records) == record_2
    assert first_by_key('age', 'desc', records) == record_1

    assert first_by_key('gpa', 'asc', records) == record_1
    assert first_by_key('gpa', 'desc', records) == record_2

    assert first_by_key('rank', 'asc', records) == record_1
    assert first_by_key('rank', 'desc', records) == record_2

    record_1 = {'age': 10, 'gpa': -2, 'rank': 1}
    record_2 = {'age': 1, 'gpa': 3, 'rank': 4}
    record_3 = {'age': 20}
    records = [record_1, record_2, record_3]

    assert first_by_key('gpa', 'asc', records) == record_1
    assert first_by_key('gpa', 'desc', records) == record_2

    assert first_by_key('rank', 'asc', records) == record_3
    assert first_by_key('rank', 'desc', records) == record_2

    assert first_by_key('gpa', 'asc', []) == {}


def get_min_by_key(records, key):
    """
    result = {}
    if not records:
        return result
    min_so_far = inf
    for record in records:
        value = record.get(key, 0)
        if value < min_so_far:
            min_so_far = value
            result = record
    return result
    """
    return first_by_key(key, "asc", records)

def test_get_min_by_key():
    record_1 = {'age': 10, 'gpa': 2, 'rank': 1}
    record_2 = {'age': 1, 'gpa': 3, 'rank': 4}
    records = [record_1, record_2]
    assert get_min_by_key(records, 'age') == record_2
    assert get_min_by_key(records, 'gpa') == record_1
    assert get_min_by_key(records, 'rank') == record_1

    record_1 = {'age': 10, 'gpa': -2, 'rank': 1}
    record_2 = {'age': 1, 'gpa': 3, 'rank': 4}
    record_3 = {'age': 20}
    records = [record_1, record_2, record_3]

    assert get_min_by_key(records, 'gpa') == record_1
    assert get_min_by_key(records, 'rank') == record_3

    assert get_min_by_key([], 'gpa') == {}

if __name__=='__main__':
    test_get_min_by_key()
    test_get_first_by_key()

