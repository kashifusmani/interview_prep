
def length_each_scene(input_list):
    rev_list = input_list[::-1]
    result = []
    i = 0
    x = 0
    while i < len(input_list):
        elem = input_list[i]
        rev_index = rev_list.index(elem)
        last_index = len(input_list) - 1 - rev_index
        elems = set(input_list[i:last_index+1])
        x = i
        for j in range(last_index, len(input_list)):
            if input_list[j] not in elems:
                break
            j += 1
            x = j
        result.append(len(input_list[i:x]))
        i = i + x
    if x < len(input_list):
        result.append(len(input_list[x:]))
    return result


if __name__ == '__main__':
    shots1 = ['a','b','a','b','c','b','a','c','a','d','e','f','e','g','d','e','h','i','j','h','k','l','i','j']
    actual1 = length_each_scene(shots1)
    expected1 = [9,7,8]
    assert(actual1 == expected1)

    shots2 = ['a','b','c']
    actual2 = length_each_scene(shots2)
    expected2 = [1,1,1]
    assert(actual2 == expected2)

    shots3 = ['a','b','c', 'a']
    actual3 = length_each_scene(shots3)
    expected3 = [4]
    assert(actual3 == expected3)