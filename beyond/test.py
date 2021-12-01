def find_duplicate(arr):
    s = set()
    for elem in arr:
        if elem not in s:
            s.add(elem)
        else:
            return elem


def find_missing(arr):
    return 0


if __name__ == "__main__":
    a = [1, 4, 2, 0, 4, 5]
    print(find_duplicate(a))
