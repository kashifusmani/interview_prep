def getMinimumUniqueSum(arr):
    seen = set()
    for elem in arr:
        if elem not in seen:
            seen.add(elem)
        else:
            x = elem
            while x in seen:
                x = x + 1
            seen.add(x)
    return sum(seen)