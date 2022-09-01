class Solution:
    def nearestValidPoint(self, x, y, points) -> int:
        smallest_index = -1
        smallest_manhattan = -1
        for i, elem in enumerate(points):
            if self.is_valid(x, y, elem[0], elem[1]):
                print(str(i)  + "is valid")
                if smallest_index == -1:
                    smallest_manhattan = self.cal_manhattan(x, y, elem[0], elem[1])
                    smallest_index = i
                else:
                    new_dist = self.cal_manhattan(x, y, elem[0], elem[1])
                    if new_dist < smallest_manhattan:
                        smallest_manhattan = new_dist
                        smallest_index = i
        return smallest_index


    def is_valid(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        return (x1 == x2) or (y1 == y2)

    def cal_manhattan(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x1 - x2) + abs(y1 - y2)
