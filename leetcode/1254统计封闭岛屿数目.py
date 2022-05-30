"""
二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。

请返回 封闭岛屿 的数目

"""
from typing import List


class Solution:

    def __init__(self):
        self.grid = None
        self.lens_i = None
        self.lens_j = None
        self.walked = set()

    def search(self, i, j):
        self.walked.add((i, j))
        if self.grid[i][j] == 1:
            return True
        if i == 0 or j == 0 or i == self.lens_i - 1 or j == self.lens_j - 1:
            return False
        res_up = self.search(i - 1, j) if (i - 1, j) not in self.walked else True
        res_down = self.search(i + 1, j) if (i + 1, j) not in self.walked else True
        res_left = self.search(i, j - 1) if (i, j - 1) not in self.walked else True
        res_right = self.search(i, j + 1) if (i, j + 1) not in self.walked else True
        return res_up & res_down & res_left & res_right

    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        self.grid = grid
        self.lens_i = len(grid)
        self.lens_j = len(grid[0])
        for i in range(1, self.lens_i - 1):
            for j in range(1, self.lens_j - 1):
                if grid[i][j] == 1:
                    continue
                else:
                    if (i, j) not in self.walked and self.search(i, j):
                        res += 1
        print(res)
        return res


if __name__ == '__main__':
    s = Solution()
    data = [[1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 1, 0, 1, 0, 1, 0, 0, 1, 0]]
    s.closedIsland(data)
