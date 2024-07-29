
def compute_penalties(log):
    customers = log.split(" ")
    open_after = [0 for _ in range(len(customers) + 1)]
    closed_until = [0 for _ in range(len(customers) + 1)]

    for i in range(0, len(customers)):
        elem = customers[i]
        if elem == 'N':
            closed_until[i+1] = closed_until[i] + 1
        else:
            closed_until[i+1] = closed_until[i]

    for i in range(0, len(customers)):
        elem = customers[len(customers)-1 -i ]
        if elem == 'Y':
            open_after[len(customers)-1 -i ] = open_after[len(customers) -i ] + 1
        else:
            open_after[len(customers)-1 -i ] = open_after[len(customers) -i ]


    penalties = []

    for i in range(0, len(open_after)):
        penalties.append(open_after[i] + closed_until[i])

    return penalties


def compute_penalty(log, hour):
    penalties = compute_penalties(log)
    return(penalties[hour])

def find_best_closing_time(log):
    penalties = compute_penalties(log)
    min_hour = len(penalties)
    min_penalty = len(penalties)

    for i in range(0, len(penalties)):
        if penalties[i] < min_penalty:
            min_penalty = penalties[i]
            min_hour = i
    return min_hour

def get_best_closing_times(log):
    log = log.replace('\n', '').split(' ')

    valid_logs = []

    window_start = -1
    window_end = -1

    i = 0

    while i < len(log):
        if log[i] == 'BEGIN':
            window_start = i
        elif log[i] == 'END':
            window_end = i

            if window_start != -1 and window_end != -1 and window_start < window_end:
                valid_log = log[window_start + 1: window_end]
                valid_logs.append(valid_log)
                window_start = -1
                window_end = -1

        i += 1

    result = []
    for v in valid_logs:

        result.append(find_best_closing_time(" ".join(v)))

    return result


if __name__ == '__main__':
    assert compute_penalty("Y Y N Y", 0) == 3
    assert compute_penalty("N Y N Y", 2) == 2
    assert compute_penalty("Y Y N Y", 4) == 1

    assert compute_penalty("Y Y N Y" , 1) == 2
    assert compute_penalty("Y Y Y N N N N" , 0) == 3
    assert compute_penalty("Y Y Y N N N N" , 7) == 4

    assert compute_penalty("Y Y Y N N N N" , 3) == 0
    assert compute_penalty("", 0) == 0
    assert compute_penalty("Y N Y N N N N" , 3) == 1

    assert find_best_closing_time("Y Y N N") == 2
    assert find_best_closing_time("N N N N") == 0
    assert find_best_closing_time("Y Y Y Y") == 4

    assert find_best_closing_time("") == 0

    assert find_best_closing_time("Y") == 1
    assert find_best_closing_time("N") == 0

    assert find_best_closing_time("N Y Y Y Y N N N Y N N Y Y N N N N Y Y N N Y N N N" ) == 5
    assert find_best_closing_time("N N N N N Y Y Y N N N N Y Y Y N N N Y N Y Y N Y N" ) == 0
    assert find_best_closing_time("Y Y N N N Y Y N Y Y N N N Y Y N N Y Y Y N Y N Y Y" ) == 25

    assert find_best_closing_time("Y Y Y N N N N") == 3

    assert get_best_closing_times("BEGIN Y Y END \nBEGIN N N END") == [2, 0]
    assert get_best_closing_times("BEGIN BEGIN \nBEGIN N N BEGIN Y Y\n END N N END") == [2]

    assert get_best_closing_times("BEGIN Y Y END \nBEGIN N N END") == [2, 0]
    assert get_best_closing_times("BEGIN BEGIN \nBEGIN N N BEGIN Y Y\n END N N END") == [2]
    assert get_best_closing_times("END BEGIN \nBEGIN N N BEGIN Y Y\n END N N END") == [2]
