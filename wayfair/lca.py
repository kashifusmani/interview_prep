'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

             15
             |
         14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
   (12, 9), (15, 13)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

has_common_ancestor(parent_child_pairs_1, 3, 8) => false
has_common_ancestor(parent_child_pairs_1, 5, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 9) => true
has_common_ancestor(parent_child_pairs_1, 1, 3) => false
has_common_ancestor(parent_child_pairs_1, 3, 1) => false
has_common_ancestor(parent_child_pairs_1, 7, 11) => true
has_common_ancestor(parent_child_pairs_1, 6, 5) => true
has_common_ancestor(parent_child_pairs_1, 5, 6) => true


Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
 \ /    / \
  3    6   7
   \        \
    4        8

parent_child_pairs_2 = [
    (1, 3), (11, 10), (11, 12), (2, 3), (10, 2),
    (10, 5), (3, 4), (5, 6), (5, 7), (7, 8),
]

has_common_ancestor(parent_child_pairs_2, 4, 12) => true
has_common_ancestor(parent_child_pairs_2, 1, 6) => false
has_common_ancestor(parent_child_pairs_2, 1, 12) => false

n: number of pairs in the input

'''

parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
    (15, 13)
]

parent_child_pairs_2 = [
    (1, 3), (11, 10), (11, 12), (2, 3), (10, 2),
    (10, 5), (3, 4), (5, 6), (5, 7), (7, 8)
]



def findAllParents(tree, nodeA):
    result = set()
    # return all the parents of nodeA
    for elem in tree:
        values = tree[elem]
        if nodeA in values:
            result.add(elem)
            for par in findAllParents(tree, elem):
                result.add(par)

    return result


def has_common_ancestor(elems, nodeA, nodeB):
    tree = {}
    visited = {}
    for (i, j) in elems:
        if i not in tree:
            tree[i] = {j}
        else:
            tree[i].add(j)
        visited[i] = False

    for elem in tree.values():
        if nodeA in elem and nodeB in elem:
            return True

    parentsNodeA = findAllParents(tree, nodeA)
    parentsNodeB = findAllParents(tree, nodeB)

    if len(parentsNodeA.intersection(parentsNodeB)) > 0:
        return True

    return False


if __name__ == '__main__':
    assert(has_common_ancestor(parent_child_pairs_1, 3, 8) == False)
    assert(has_common_ancestor(parent_child_pairs_1, 5, 8) == True)
    assert(has_common_ancestor(parent_child_pairs_1, 6, 8) == True)
    assert(has_common_ancestor(parent_child_pairs_1, 6, 9) == True)
    assert(has_common_ancestor(parent_child_pairs_1, 1, 3) == False)
    assert(has_common_ancestor(parent_child_pairs_1, 3, 1) == False)
    assert(has_common_ancestor(parent_child_pairs_1, 7, 11) == True)
    assert(has_common_ancestor(parent_child_pairs_1, 6, 5) == True)
    assert(has_common_ancestor(parent_child_pairs_1, 5, 6) == True)
    assert(has_common_ancestor(parent_child_pairs_2, 4, 12) == True)
    assert(has_common_ancestor(parent_child_pairs_2, 1, 6) == False)
    assert(has_common_ancestor(parent_child_pairs_2, 1, 12) == False)
