# Time space O(n), space O(n)
def compress(s):
    if len(s) == 0:
        return ''

    result = [] #Use list instead of string since strings are immutable, hence space complexity will be huge
    elem_count = 1
    prev_elem = s[0]
    for elem in s[1:]:
        if prev_elem == elem:
            elem_count += 1
        else:
            result.append(prev_elem + str(elem_count))
            prev_elem = elem
            elem_count = 1
    result.append(prev_elem + str(elem_count))
    return ''.join(result)


if __name__ == '__main__':
    print(compress('AAAAABBBBCCCC'))
    print(compress('AAB'))
    print(compress('A'))
