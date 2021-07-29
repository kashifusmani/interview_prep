#Given an integer array of the item weights, partition it into two sets S1 and S2 such that the sum of S1 is greater than that of S2. Return S1.
# If more than one such partition exists, return the one with minimal size.


def minimalHeaviestSetA(arr):
    result = []
    sort = list(reversed(sorted(arr)))
    sumA = 0
    for i in range(0, len(sort)):
        sumA += sort[i]
        result.append(sort[i])
        sumB = sum(sort[i+1:])
        if sumA >= sumB:
            break
    return list(reversed(result))


if __name__ == '__main__':
    print(minimalHeaviestSetA([5, 3, 2, 4, 1, 2]))
    print(minimalHeaviestSetA([4, 2, 5, 1, 6]))
