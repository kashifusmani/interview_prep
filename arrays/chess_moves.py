#TODO Incomplete solution
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.helper(x,y)

    def helper(self, x: int, y:int) -> int:
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for a,b in moves:
            [is_p, steps] = self.is_possible(a, b, x, y, 0)
            if is_p:
                return steps

    def is_possible(self, a, b, x, y, steps):
        if x == a and y == b:
            return [True, steps]
        if x < a or y < b:
            return [False, 0]
        else:
            return self.is_possible(a, b, abs(x - abs(a)), abs(y - abs(b)), steps+1)

if __name__ == '__main__':
    s = Solution()
    s.minKnightMoves(2,1)