"""
/*
Imagine we have an image. We'll represent this image as a simple 2D array where every pixel is a 1 or a 0.
The image you get is known to have potentially many distinct rectangles of 0s on a background of 1's.
Write a function that takes in the image and returns the coordinates of all the 0 rectangles
-- top-left and bottom-right; or top-left, width and height.
image1 = [
  [0, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1, 0],
]
Sample output variations (only one is necessary):
findRectangles(image1) =>
  // (using top-left-row-column and bottom-right):
  [
    [[0,0],[0,0]],
    [[2,0],[2,0]],
    [[2,3],[3,5]],
    [[3,1],[5,1]],
    [[5,3],[6,4]],
    [[7,6],[7,6]],
  ]
  // (using top-left-row-column and width/height):
  [
    [[0,0],[1,1]],
    [[2,0],[1,1]],
    [[2,3],[3,2]],
    [[3,1],[1,3]],
    [[5,3],[2,2]],
    [[7,6],[1,1]],
  ]
Other test cases:
image2 = [
  [0],
]
findRectangles(image2) =>
  // (using top-left-row-column and bottom-right):
  [
    [[0,0],[0,0]],
  ]
  // (using top-left-row-column and width/height):
  [
    [[0,0],[1,1]],
  ]
image3 = [
  [1],
]
findRectangles(image3) => []
image4 = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1],
]
findRectangles(image4) =>
  // (using top-left-row-column, and bottom-right or width/height):
  [
    [[1,1],[3,3]],
  ]
n: number of rows in the input image
m: number of columns in the input image """


def helper(i, j, matrix):
    x = i
    y = j
    for k in range(i+1, len(matrix)):
        if matrix[k][y] == 0:
            x = k
        else:
            break
    for k in range(j+1, len(matrix[x])):
        if matrix[x][k] == 0:
            y = k
        else:
            break
    return [x, y]


def coord_in_rectangle(result, i, j):
    for entry in result:
        start = entry[0]
        end = entry[1]
        if start[0] <= i <= end[0] and start[1] <=j <= end[1]:
            return True
    return False


def find_squares(matrix):
    result = []
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item == 0 and not coord_in_rectangle(result, i, j):
                start = [i, j]
                end = helper(i, j, matrix)
                result.append([start, end])
    return result


if __name__ == '__main__':
    parent_child_pairs_1 = [
        (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
        (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
        (15, 13)
    ]

    for (x,y) in parent_child_pairs_1:
        print(x)
        print(y)
        print('==')

    sample1 = [
        [0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 1]caree
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0]
    ]
    expected1 = [
        [[0,0],[0,0]],
        [[2,0],[2,0]],
        [[2,3],[3,5]],
        [[3,1],[5,1]],
        [[5,3],[6,4]],
        [[7,6],[7,6]],
    ]
    assert(find_squares(sample1) == expected1)

    sample2 = [
        [0,0],[0,0]
    ]
    expected2 = [
        [[0,0],[1,1]]
    ]
    result2 = find_squares(sample2)
    assert(result2 == expected2)

    sample3 = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]
    expected3 = [
        [[1,1],[3,3]],
    ]
    result3 = find_squares(sample3)
    assert(result3 == expected3)
