def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
    max_sum = current_sum = arr[0]
    start = end = 0

    for ind, elem in enumerate(arr[1:]):
        if current_sum + elem > elem:
            current_sum = current_sum + elem
        else:
            current_sum = elem # If current + elem is less than the elem itself ( because elem is negative), better to reset the current_sum
            start = ind + 1 #Since sum is reset, restart the index here

        if max_sum < current_sum:
            max_sum = current_sum #Since max_sum is reset here, reset the end here.
            end = ind + 1

    return (start,end, max_sum)


if __name__ == "__main__":
    arr = [-2,-3,4,-1,-2,1,5,-3]
    arr_2 = [1,2,-1,3,4,-1]
    arr_3 = [1,2,-1,3,4,10,10,-10, -1]
    start,end, max_sum = large_cont_sum(arr_3)
    print(start)
    print(end)
    print(max_sum)
