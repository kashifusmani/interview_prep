'''
Write a function(int[]) -> int that returns the lowest unassigned integer.  For example [] -> 1 (empty set), [1] -> 2, [5, 3, 1] -> 2.
Basically just sort the array, iterate, and compare current and previous.  If there is a gap then that's your number.
'''


def get_lowest_unassigned_number(inp):
    if not inp:
        return 1

    #option 1 use cyclic sort if starts with zero or 1
    #option2 use regular sort

    inp_sorted = sorted(inp)
    prev = inp_sorted[0]
    for elem in inp_sorted[1:]:
        if prev + 1 != elem:
            return prev +1
        else:
            prev = elem
    return prev+1

if __name__ == '__main__':
    assert(get_lowest_unassigned_number([])) == 1
    assert(get_lowest_unassigned_number([1])) == 2
    assert(get_lowest_unassigned_number([5, 3, 1])) == 2
    assert(get_lowest_unassigned_number([1,2, 3])) == 4

