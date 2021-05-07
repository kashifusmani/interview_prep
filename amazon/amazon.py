def storage(n, m, h, v):
    # Write your code here
    horizontal_p, vertical_p = 0, 0
    max_height, max_width = 0, 0
    previous = 0
    
    for h_coordinate in range(1, n+2):
        if h_coordinate != h[horizontal_p]:
            max_height = max(max_height, h_coordinate - previous)
            previous = h_coordinate
        else:
            if horizontal_p < len(h) - 1:
                horizontal_p += 1
    
    previous = 0
    for v_coordinate in range(1, m+1):
        if v_coordinate != v[vertical_p]:
            max_width = max(max_width, v_coordinate - previous)
            previous = v_coordinate
        else:
            if vertical_p == len(v) - 1:
                vertical_p += 1
    
    return max_height * max_width

# print(storage   (3,3,[2], [2])    )



def maxArea(h: int, w: int, horizontalCuts, verticalCuts) -> int:
    hc = set(horizontalCuts)
    vc = set(verticalCuts)
    # for height
    maxHei = 1
    prevH = 1
    for i in range(1, h+1):
        if i in hc:
            prevH += 1
        else:
            prevH = 1
        maxHei = max(maxHei, prevH)
    # print(maxHei)
    # for width
    maxWid = 1
    prevWid = 1
    for j in range(1, w+1):
        if j in vc:
            prevWid +=1
        else:
            prevWid = 1
        maxWid = max(maxWid, prevWid)
    # print(maxWid)
    return (maxWid*maxHei)%((10**9) + 7)

# print(maxArea(3,3,[2], [2])    )
# print(maxArea(3,2,[1,2,3], [1,2])    )


def optimizing_boxes(elements) :
    elements.sort()
    total = sum(elements)
    min_sum_in_a = (total // 2) + 1
    
    temp = 0
    result = []
    for i in reversed(range(len(elements))):
        temp += elements[i]
        result.insert(0, elements[i])
        
        if (temp >= min_sum_in_a) and (len(result) < len(elements) - len(result)): 
            return result
    
    return None

print(optimizing_boxes([1,1,1,1,1,1]))

def minimalHeaviestSetA(arr):
    # Write your code here
    
    result = []
    
    sort = list(reversed(sorted(arr)))
    sum_a = 0
    for i in range(0, len(sort)):
        sum_a += sort[i]
        
        result.append(sort[i])
        sum_b = sum(sort[i+1:])
        
        if sum_a >= sum_b:
            break
    
    return list(reversed(result))

print(minimalHeaviestSetA([1,1,1,1,1,1]))


def storage(n, m, h, v):
    # Write your code here
    # horizontal_p, vertical_p = 0, 0
    h = set(h)
    v = set(v)
    
    max_height, max_width = 1, 1
    previous_h, previous_w = 1, 1
    
    for h_coordinate in range(1, n+1):
        if h_coordinate in h:
            previous_h += 1
        else:
            previous_h = 1
        max_height = max(max_height, previous_h)
    
    
    for v_coordinate in range(1, m+1):
        if v_coordinate in v:
            previous_w += 1
        else:
            previous_w = 1
            
        max_width = max(max_width, previous_w)
    
    return max_height * max_width



#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimalHeaviestSetA(arr):
    
    if len(set(arr)) == 1:
        x = 0
        if len(arr) % 2 == 0:
            x = 1
        return arr[(len(arr) // 2) - x:]
        
    
    arr.sort()
    total = sum(arr)
    min_sum = (total // 2) + 1
    
    temp  = 0
    result = []
    
    for i in reversed(range(len(arr))):
        temp += arr[i]
        result.insert(0, arr[i])
        
        
        if (temp >= min_sum) and (len(result) < len(arr) - len(result)):
            return result
    
    return []

if __name__ == '__main__':    