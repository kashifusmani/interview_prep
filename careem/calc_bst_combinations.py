

'''
                 6
             3       11
                   8    13
                7

                   [[8]]    [[13]]   ==> [[11, 8, 7, 13] , [11, 13, 8, 7]]

                   [11]
                [8, 7]     [13]

                [11, 8, 7, 13]
                [11, 13, 8, 7]
                [11, 8, 13, 7]
           [[3]]          [[11, 8]]


           [[4, ,1, 5]] [[9, 8, 11]]

           [4, 1, 5] ,  [9, 8, 11]
              l1            l2
             [4] + getConstraintPermutation ([1, 5] [9, 8, 11])
             [9] + getConstraintPermutation([4, 1, 5] [8, 11])

from itertools import permutations
def getConstraintPermutation(l1, l2):
        if l1 == []:
            return l2
        if l2 == []:
            return l1
        else:
            result = []
            for item in getConstraintPermutation(l1[1:], l2):
                result.append([l1[0]] + item)
            for item in getConstraintPermutation(l1, l2[1:]):
                result.append([l2[0]] + item)
            return result



'''

'''


[4, 10, 13, 6]

[4, 10, 6, 13]

    4
  /    \
 2      10
/ \    /  \
1  3    
   
[4, 2, 10, 1, 3]
[4, 10, 2, 1, 3]

[4, 2, 10, 3, 1]
[4, 10, 2, 3, 1]

[4, 2, 3, 10, 1]


[4, 3, 10, 2, 1]
[4, 10, 3, 1, 2]

[4, 3, 10, 6, 13]
[4, 10, 3, 13, 6]

[4, 3, 10, 2, 1, 13, 6]
[4, 10, 3, 1, 2, 6, 13]

[4, 3, 10, 6, 13, 2, 1]
[4, 10, 3, 13, 6, 1, 2]


You are given a BST return all the array that would result in that BST. // THERE ARE NO DUPLICATES

'''




