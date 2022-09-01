#This solution needs to be revisited
#https://www.geeksforgeeks.org/minimum-swaps-required-group-1s-together/
def minCommon(arr):
    precomp = precompute(arr)
    numOnes = arr.count(1)

    index = numOnes-1; count = precomp[index]
    for i in range(numOnes, len(precomp)):
        running_diff  =precomp[i] - precomp[i-numOnes]
        if running_diff > count:
            count =  running_diff
            index = i
    return (index-numOnes+1, index+1)

def getIndices(arr, elem):
    return [i for i, x in enumerate(arr) if x == elem]

def calcGreaterThanIndex(arr, index):
    for k in arr:
        if k > index:
            return k

def precompute(arr, elem=1):
    result = []
    if arr[0] == elem:
        result.append(1)
    else:
        result.append(0)
    for i in range (1, len(arr)):
        if arr[i] == elem:
            result.append(result[i-1] + 1)
        else:
            result.append(result[i-1])
    return result

def minMoves(arr):
    indices = minCommon(arr)
    moves = 0
    for i in range(len(arr)):
        if i>= indices[0] and i <= indices[1]-1 and arr[i] ==0:
            one_indices = getIndices(arr, 1)
            swap_index = calcGreaterThanIndex(one_indices, indices[1]-1)
            moves += swap_index - i

            temp = arr[i]
            arr[i] = arr[swap_index]
            arr[swap_index] = temp
    return moves

if __name__ == '__main__':
    #print(ct([3,2,1,2,1,7]))
    print(minMoves([1,0,1,0,1,0,1,0]))