def findSubarrays(arr, target):
    result = []
    i = 0
    j = 0
    product = 1
    while j < len(arr):
        product *= arr[j]

        while product >= target:
            product = product/arr[i]
            i += 1

        pairs = []
        for k in range(i, j+1):
            pairs.append(arr[k])
            result.append(pairs)
        j += 1

    return result

if __name__ == '__main__':
    findSubarrays([2, 5, 3, 10], 30)