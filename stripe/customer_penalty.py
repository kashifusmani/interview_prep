'''
# For the purposes of this interview, imagine that we own a store. This
# store doesn't always have customers shopping: there might be some long
# stretches of time where no customers enter the store. We've asked our
# employees to write simple notes to keep track of when customers are
# shopping and when they aren't by simply writing a single letter every
# hour: 'Y' if there were customers during that hour, 'N' if the store
# was empty during that hour.

# For example, our employee might have written "Y Y N Y", which means
# the store was open for four hours that day, and it had customers
# shopping during every hour but its third one.

#   hour: | 1 | 2 | 3 | 4 |
#   log:  | Y | Y | N | Y |
#                   ^
#                   |
#             No customers during hour 3

# We suspect that we're keeping the store open too long, so we'd like to
# understand when we *should have* closed the store. For simplicity's
# sake, we'll talk about when to close the store by talking about how
# many hours it was open: if our closing time is `2`, that means the
# store would have been open for two hours and then closed.

#   hour:         | 1 | 2 | 3 | 4 |
#   log:          | Y | Y | N | Y |
#   closing_time: 0   1   2   3   4
#                 ^               ^
#                 |               |
#          before hour #1    after hour #4

# (A closing time of 0 means we simply wouldn't have opened the store at
# all that day.)

# First, let's define a "penalty": what we want to know is "how bad
# would it be if we had closed the store at a given hour?" For a given
# log and a given closing time, we compute our penalty like this:

#   +1 penalty for every hour that we're *open* with no customers
#   +1 penalty for every hour that we're *closed* when customers would have shopped

# For example:

#   hour:    | 1 | 2 | 3 | 4 |   penalty = 3:
#   log:     | Y | Y | N | Y |     (three hours with customers after closing)
#   penalty: | * | * |   | * |
#            ^
#            |
#          closing_time = 0

#   hour:    | 1 | 2 | 3 | 4 |   penalty = 2:
#   log:     | N | Y | N | Y |      (one hour without customers while open +
#   penalty: | * |   |   | * |       one hour with customers after closing)
#                    ^
#                    |
#                  closing_time = 2

#   hour:    | 1 | 2 | 3 | 4 |   penalty = 1
#   log:     | Y | Y | N | Y |      (one hour without customers while open)
#   penalty: |   |   | * |   |
#                            ^
#                            |
#                          closing_time = 4

# Note that if we have a log from `n` open hours, the `closing_time`
# variable can range from 0, meaning "never even opened", to n, meaning
# "open the entire time".

# 1)
# Write a function `compute_penalty` that computes the total penalty, given
#   a store log (as a space separated string) AND
#   a closing time (as an integer)

# In addition to writing this function, you should use tests to
# demonstrate that it's correct. Do some simple testing, and then quickly
# describe a few other tests you would write given more time.

# ## Examples

# compute_penalty("Y Y N Y", 0) should return 3
# compute_penalty("N Y N Y", 2) should return 2
# compute_penalty("Y Y N Y", 4) should return 1

# 2)
# Write another function named `find_best_closing_time` that returns
# the best closing time in terms of `compute_penalty` given just a
# store log. You should use your answer from part 1 to solve this problem.


# Again, you should use tests to demonstrate that it's correct. Do
# some simple testing, and then quickly describe a few other tests
# you would write given more time.

# ## Example
# find_best_closing_time("Y Y N N") should return 2

# 3)

# We've asked our employees to write their store logs all together in the
# same text file, marking the beginning of each day with `BEGIN` and the
# end of each day as `END`, sometimes spanning multiple lines. We hoped
# that the file might look like

#   "BEGIN Y Y END \nBEGIN N N END"

# which would represent two days, where the store was open two hours
# each day. Unfortunately, our employees are often too busy to remember
# to finish the logs, which means this text file is littered with
# unfinished days and extra information scattered throughout. Luckily,
# we know that an unbroken sequence of BEGIN, zero or more Y's or N's,
# and END is going to be a valid log, so we can search the aggregate log
# for those.

# For example, given the aggregate log:

#   "BEGIN BEGIN BEGIN N N BEGIN Y Y END N N END"
#                          ^           ^
#                          |           |
#                          +-----------+
#                            valid log

# In this example, We can extract only one valid log, "BEGIN Y Y END". For our
# purposes, we should ignore any invalid log. *A valid log cannot contain a
# nested log. (i.e. Valid logs cannot be nested.) Valid logs can span multiple lines.
# Also there can be multiple valid logs on a single line.*

# Write a function `get_best_closing_times` that takes an aggregate log
# as a string and returns an array of best closing times for every valid
# log we can find, in the order that we find them.

# Again, you should use tests to demonstrate that it's correct. Do
# some simple testing, and then quickly describe a few other tests
# you would write given more time.

# ## Examples
# get_best_closing_times("BEGIN Y Y END \nBEGIN N N END")
#   should return an array: [2, 0]
# get_best_closing_times("BEGIN BEGIN \nBEGIN N N BEGIN Y Y\n END N N END")
#   should return an array: [2]

from array import array


def compute_penalty(log: str, closing_time: int) -> int:
    hours = log.split()
    penalty = 0

    for i in range(len(hours)):
        if i < closing_time:
            if hours[i] == "N":
                penalty += 1
        else:
            if hours[i] == "Y":
                penalty +=1

    return penalty

assert compute_penalty("Y Y N Y", 0) == 3
assert compute_penalty("N Y N Y", 2) == 2
assert compute_penalty("Y Y N Y", 4) == 1

assert compute_penalty("Y Y Y Y", 0) == 4
assert compute_penalty("N N N N", 0) == 0

print("test_compute_penalty")
assert compute_penalty("Y Y N Y" , 1) == 2
assert compute_penalty("Y Y Y N N N N" , 0) == 3
assert compute_penalty("Y Y Y N N N N" , 7) == 4
assert compute_penalty("Y Y Y N N N N" , 3) == 0
assert compute_penalty("", 0) == 0
assert compute_penalty("Y N Y N N N N" , 3) == 1


def find_best_closing_time(log: str) -> int:
    hours = log.split()
    best_penalty = float('inf')
    best_closing_time = -1

    for i in range(len(hours) + 1):
        penalty = compute_penalty(log, i)

        if penalty < best_penalty:
            best_penalty = penalty
            best_closing_time = i

    return best_closing_time


assert find_best_closing_time("Y Y N N") == 2
assert find_best_closing_time("N Y N N") == 0
assert find_best_closing_time("N N N N") == 0
assert find_best_closing_time("Y Y Y Y") == 4
assert find_best_closing_time("N N Y Y") == 0
assert find_best_closing_time("") == 0

print("test_find_best_closing_time")
assert find_best_closing_time("Y Y Y N N N N" ) == 3
assert find_best_closing_time("") == 0
assert find_best_closing_time("Y") == 1
assert find_best_closing_time("N N N N" ) == 0
assert find_best_closing_time("Y Y Y Y" ) == 4
assert find_best_closing_time("N Y Y Y Y N N N Y N N Y Y N N N N Y Y N N Y N N N" ) == 5
assert find_best_closing_time("N N N N N Y Y Y N N N N Y Y Y N N N Y N Y Y N Y N" ) == 0
assert find_best_closing_time("Y Y N N N Y Y N Y Y N N N Y Y N N Y Y Y N Y N Y Y" ) == 25



def get_best_closing_times(log: str) -> list:
    best_closing_times = []
    counter = 0
    while counter < range(len(log)):
        if log[i] == "B":


    return best_closing_times

assert get_best_closing_times("BEGIN Y Y END \nBEGIN N N END") == [2, 0]
assert get_best_closing_times("BEGIN BEGIN \nBEGIN N N BEGIN Y Y\n END N N END") == [2]
assert get_best_closing_times("END BEGIN \nBEGIN N N BEGIN Y Y\n END N N END") == [2]



'''
def bestClosingTime(customers: str) -> int:
    open_after = [0 for _ in range(len(customers) + 1)]
    closed_until = [0 for _ in range(len(customers) + 1)]

    for i in range(0, len(customers)):
        elem = customers[i]
        if elem == 'N':
            closed_until[i+1] = closed_until[i] + 1
        else:
            closed_until[i+1] = closed_until[i]

    for i in range(0, len(customers)):
        elem = customers[len(customers)-1-i]
        if elem == 'Y':
            open_after[len(customers) - i - 1] =  open_after[len(customers) - i] + 1
        else:
            open_after[len(customers) - i - 1] =  open_after[len(customers) - i]


    min_hour = len(customers)
    min_penalty = len(customers)


    for i in range(len(customers) + 1):
        penalty = open_after[len(customers) - i] + closed_until[len(customers) - i]
        if penalty <= min_penalty:
            min_penalty = penalty
            min_hour = len(customers) - i
    return min_hour


def get_best_closing_times(log):
    log = log.replace('\n', '').split(' ')
    print(log)

    window_start = -1
    window_end = -1

    valid_logs = []

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
        result.append(bestClosingTime(v))
    print(result)