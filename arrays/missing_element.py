# O(n) BUT it has problems
# 1. If the arrays are too large, then sum will overflow
# 2. If the numbers are too small and havea lots of decimal places, then you will lose some information
def finder(arr1, arr2):
    return sum(arr1) - sum(arr2)

#using sort (NLogN), space O(n)
def finder_4(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    for a,b in zip(arr1, arr2):
        if a != b:
            return a
    return arr1[-1]

#Using count dictionary o(N), space O(N)
import collections
def finder_2(arr2, arr1):
    d = collections.defaultdict(int)
    for num in arr1:
        d[num] += 1

    for num in arr2:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

#Using Exclusive OR
# O(n) and constant space
def finder_3(arr1, arr2):
    counter = 0
    for elem in arr1 + arr2:
        counter = counter ^ elem
    return counter


if __name__ == '__main__':
    print(finder_4([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
    print(finder_4([5,5,7,7], [5,7,7]))