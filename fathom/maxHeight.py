

def maxHeight(wallPositions, wallHeights):
    arr = [0] * (wallPositions[-1])

    for x,y in zip(wallPositions, wallHeights):
        arr[x-1] = y

    max_height = 0
    for i in range(0, len(arr)):
        if arr[i] == 0:
            max_index, next_non_zero_at_right = next_non_zero(arr[i+1:])
            new_height = min(next_non_zero_at_right+2, arr[i-1]+1)
            if new_height - (next_non_zero_at_right + max_index )> 1:
                new_height = next_non_zero_at_right + 1
            arr[i] = new_height
            if new_height > max_height:
                max_height = new_height

    return max_height


def next_non_zero(arr):
    for i, elem in enumerate(arr):
        if elem > 0:
            return (i, elem)


if __name__ == '__main__':
    print(maxHeight([1,3,7], [4,3,3]))
    print(maxHeight([1,10], [1,5]))
