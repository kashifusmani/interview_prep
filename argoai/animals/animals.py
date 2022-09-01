#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY predators as parameter.
#

# {predator=value: prey=i for i, value in enumerate(predators)}


def getLevel(predators):
    result = []
    for index, item in enumerate(predators):
        level = 0
        if item == -1:
            result.append(level)
        else:
            temp_item = item
            predator = predators[temp_item]
            level += 1
            while predator!= -1:
                predator = predators[predator]
                level += 1
                temp_item = predator
            result.append(level)

    return result


def minimumGroups(predators):
    return(max(getLevel(predators)) + 1)

if __name__ == '__main__':
    print(minimumGroups([-1, 8, 6, 0, 7, 3, 8, 9, -1, 6]))