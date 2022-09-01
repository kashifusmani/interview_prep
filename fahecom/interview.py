"""
Write Python code to find 3 words that occur together most often?
Given input:
There is the variable input that contains words separated by a space.
The task is to find out the three words that occur together most often (order does not matter)
input = "cats milk jump bill jump milk cats dog cats jump milk"

"""
from collections import defaultdict

def algo(input, words_len=3):
    result = {}
    if len(input) < words_len:
        pass
    if len(input) == words_len:
        result = {make_key(input): 1}
    else:
        start = 0

        while start+words_len < len(input):
            current_set = sorted(input[start:start+words_len])
            our_key = make_key(current_set)
            if our_key in result:
                start += 1
                continue
            else:
                result[our_key] = 1
            print(current_set)
            inner_start = start + 1
            while inner_start+words_len < len(input):
                observation_set = sorted(input[inner_start:inner_start+ words_len])
                if current_set == observation_set:
                    check(our_key, result)
                inner_start += 1
            observation_set = sorted(input[inner_start:])
            if current_set == observation_set:
                check(our_key, result)
            start += 1
    return result


def make_key(input):
    return ','.join(input)


def check(our_key, result):
    if our_key in result:
        result[our_key] += 1
    else:
        result[our_key] = 1

if __name__ == '__main__':
    input = "cats milk jump bill jump milk cats dog cats jump milk"
    print(algo(input.split(" ")))

# Difference between tuple and list
# What is a generator and why is it efficient
# What is a decorator, how it works.
# select player_id, min(event_date) as first_login from activity group by player_id order by player_id asc

# with x as (select count(*) as total_logins, month-year(login_date) as month_year from logins group by month_year order by month_year asc),
# with y as (select total_logins, month_year, row_number() as row),
# select month_year, (b.total_logins - a.total_logins)/a.total_logins from
# ( select  total_logins, month_year, row from y) as a, ( select  total_logins, month_year, row from y) as b where a.row + 1 = b.row
#

# with x as (select count(*) as num_direct_report, manager_id from employee group by manager_id where num_direct_report >=5)
# select name from employee join x on employee.id=x.manager_id