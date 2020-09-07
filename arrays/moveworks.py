# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from datetime import datetime, timedelta
date_fmt = '%Y%M%d' # %Y%m%d

def solution(A):



    if len(A) <2:
        return 0


    valid_dates = []

    i = 0

    while(i<len(A)):
        if(valid(A[i], A[i+1])):
            valid_dates.append((convert(A[i]), convert(A[i+1])-timedelta(days=1)))
            # data_structure.find_upper()
            # # data_structure.find_lower()
            # Doesn't overlap
            # insertion
        i = i+2

    if len(valid_dates) == 0:
        return 0

    start = valid_dates[0][0]
    end = valid_dates[0][1]
    total_valid = 1

    for elem in valid_dates[1:]:
        if elem[0] >= end:
            end = elem[1]
            total_valid += 1
        elif start > elem[0] and start < elem[1]:
            total_valid += 1
            start = elem[0]
    print(total_valid)
    return total_valid

def convert(dateStr):
    return datetime.strptime(dateStr, date_fmt)

def valid(dateStrA, dateStrB):
    dateA = datetime.strptime(dateStrA, date_fmt)
    dateB = datetime.strptime(dateStrB, date_fmt)
    return dateA < dateB