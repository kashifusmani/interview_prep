import sys
from time import time
class Solution:
    def minTrioDegree(self, n, edges) -> int:
        min_degree = sys.maxsize

        graph = [[0]*n for i in range(n)]
        degrees = {}

        for x,y in edges:
            graph[x-1][y-1] = 1
            graph[y-1][x-1] = 1
            if x in degrees:
                degrees[x] += 1
            else:
                degrees[x] = 1
            if y in degrees:
                degrees[y] += 1
            else:
                degrees[y] = 1

        num_trios = 0
        for i in range(0, n):
            for j in range(0, n):
                if graph[i][j] == 1:
                    for k in range(j+1, n):
                        if graph[i][k] == 1 and graph[j][k] == 1:
                            num_trios += 1
                            min_degree = min(min_degree, degrees[i+1] + degrees[j+1] + degrees[k+1] - 6)
        if num_trios == 0:
            min_degree = -1
        return min_degree


    def minTrioDegreeMoreEfficient(self, n, edges) -> int:
        g = [set() for _ in range(n + 1)]
        deg = [0] * (n + 1)
        for u, v in edges:
            g[min(u, v)].add(max(u, v))
            deg[u] += 1
            deg[v] += 1
        ans = float('inf')
        for x in range(1, n + 1):
            for y in g[x]:
                for z in g[x]:
                    if y != z and z in g[y]:
                        ans = min(ans, deg[x] + deg[y] + deg[z] - 6)
        return ans if ans < float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    n = 6
    ls = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
    start = time()
    print(s.minTrioDegree(n, ls))
    end = time()

    print(end - start)