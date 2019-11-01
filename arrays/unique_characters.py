def uni_chr(s):
    res = set()
    for elem in s:
        if elem not in res:
            res.add(elem)
        else:
            return False
    return True


def uni_chr_2(s):
    return len(set(s)) == len(s)


if __name__ == '__main__':
    print(uni_chr(''))
    print(uni_chr(''))