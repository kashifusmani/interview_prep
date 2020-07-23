'''

# Input: num = "1432219", k = 3
# Output: "1219"

Input: 55023, k = 3
Output = 3




Q2


Odin was a prisoner in mythland. Though Odin was a witty and intelligent guy. He was confident of escaping prison. After few days of observation, He figured out that the prison consists of (NXN) cells.i.e The shape of prison was (NXN) matrix. Few of the cells of the prison contained motion detectors. So Odin planned that while escaping the prison he will avoid those cells containing motion detectors.Yet before executing his plan, Odin wants to know the total number of unique possible paths which he can take to escape the prison.Initially Odin is in cell
(1,1) while the exit of the cell (NXN).

note:->Odin can move in all four direction{ if his current location is (X,Y), he can move to either
(X+1,Y), (X-1,Y), (X,Y+1), (X,Y-1) }. If the first cell (1,1) and the last cell(N,N) contain motion detectors, then Odin can't break out of the prison.

Input : 2 D array of zero and and the size of array as N

prison_ex_1 = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 1, 0]]
Output 2

[0 1 1 0]
[0 0 1 0]
[0 0 0 0]
[0 1 1 0]

'''

def find_exit_path_helper(matrix, i, j, n, total_paths, visited):
    if i == n-1 and j == n-1:
        total_paths += 1
        return total_paths

    if 0<= i< n and 0 <=j <n and not visited[i][j] and matrix[i][j] == 0:
        visited[i][j] = True
        for (x,y) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            total_paths = find_exit_path_helper(matrix, x, y, n, total_paths, visited)
        visited[i][j] = False
    return total_paths


def find_exit_path(matrix, n):
    visited = [[False] *n for i in range(n)]
    if matrix[0][0] == 1 or matrix[n-1][n-1] == 1:
        return 0
    else:
        return find_exit_path_helper(matrix, 0, 0, n, 0, visited)


matrix = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 1, 0]]
matrix = [[0, 0, 0, 1], [0, 0, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0]]
print(find_exit_path(matrix, 4))

def smallest_possible(num_str, k):
    if len(num_str) == k:
        return "0"

    stack = []
    j = 0
    i = k


    while(j < len(num_str)):
        while(i> 0 and len(stack) > 0 and stack[len(stack)-1] > num_str[j]):
            stack.pop()
            i = i - 1
        stack.append(num_str[j])
        j = j+1

    while(i > 0):
        stack.pop()
        i = i-1

    #return_num = str(stack)

    #while(len(stack) > 1 and stack[0] == '0'):
    #del stack[0]

    return str(stack)





