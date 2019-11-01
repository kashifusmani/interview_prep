def is_anagram(a,b):
    counts = {}
    chars_to_ignore = ['.', ' ']
    for char in chars_to_ignore:
        a = a.replace(char, '')
        b = b.replace(char, '')
    a = a.lower()
    b = b.lower()
    if len(a) != len(b):
        return False
    for char in a:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    for char in b:
        if char not in counts:
            return False
        else:
            counts[char] -= 1

    for char in counts:
        if counts[char] > 0:
            return False
    return True

if __name__ == '__main__':
    print(is_anagram('public relations', 'crap built on lies'))
    print(is_anagram('clint eastwood', 'old west action'))
    #print(is_anagram('123', '1 2'))