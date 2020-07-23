


def programming_contest(arr):
    sorted_arr = sorted(arr)
    i = len(sorted_arr) - 1
    result = 0
    while i >=0:
        result = result + sorted_arr[i] - sorted_arr[i-1]
        i = i -2
    return result


def disk_space_analysis(segment_len, space):
    max_overall = min(space[0:segment_len])
    for i in range(1, len(space) - segment_len):
        max_overall = max(max_overall,  min(space[i:segment_len+i]))
    return max_overall


if __name__ == '__main__':
    #arr = [2,4,5,3,7,8]
    #print(programming_contest(arr))
    print(disk_space_analysis(2, [8,2,4]))
    print(disk_space_analysis(1, [1,2,3,1,2]))
    print(disk_space_analysis(2, [1,1,1]))
    print(disk_space_analysis(3, [2,5,4,6,8]))