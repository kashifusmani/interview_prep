


def binary_search(arr, elem):
    lo = 0
    hi = len(arr) - 1
    mid = -1
    while lo < hi:
        mid = (hi + lo)//2
        if elem == arr[mid]:
            return mid
        elif elem > arr[mid]:
            lo = mid+ 1
        elif elem < arr[mid]:
            hi = mid-1
    return mid -1  if elem<arr[mid] else mid

if __name__ == '__main__':
    assert (binary_search([1,2,3,4,6], 3) == 2)
    assert (binary_search([1,2,4,6], 3) == 1)

    assert (binary_search([1,3,4,6], 2) == 0)
    assert (binary_search([1,3,4,6], 0) == 0)

    assert (binary_search([0,3,5,7], 6) == 2)

    assert (binary_search([0,3,5,7], 7) == 3)


    assert (binary_search([0,3,5,7], 8) == 3)
