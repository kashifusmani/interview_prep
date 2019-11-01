#O(n^2)
def pair_sum(arr,sum):
    result = []
    for i in range(len(arr)):
        for k in range(i+1, len(arr)):
            if (arr[i] + arr[k] == sum):
                result.append((arr[i], arr[k]))
    return len(result)

#O(n)
def pair_sum_2(arr, sum):
    if len(arr) <2:
        return
    seen = set()
    output = set()

    for i in arr:
        target = sum - i
        if target not in seen:
            seen.add(i)
        else:
            output.add((min(i, target), max(i, target)))
    return output

if __name__ == '__main__':
    print(pair_sum_2([1,3,2,2], 4))
    print(pair_sum_2([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10))
    print(pair_sum_2([1,2,3,1], 3))