"""
给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        s_i = s_j = 0
        lens_i = len(grid)
        lens_j = len(grid[0])
        for r in range(lens_i):
            for c in range(lens_j):
                if grid[r][c] == 1:
                    s_i, s_j = r, c
                    break

        stack = list()
        walked = set()
        stack.append((s_i, s_j))
        res = 0

        while stack:
            i, j = current_site = stack.pop()
            walked.add(current_site)

            next_site = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for m, n in next_site:
                if m < 0 or n < 0 or m >= lens_i or n >= lens_j:
                    print("next outsize:", (m, n), "+1")
                    res += 1
                else:
                    if grid[m][n] == 0:
                        print("next water:", (m, n), "+1")
                        res += 1
                    else:
                        if (m, n) not in walked and (m, n) not in stack:
                            print("next append:", (m, n))
                            stack.append((m, n))
        print(res)
        return res


if __name__ == '__main__':
    data = [[1,1],[1,1]]
    s = Solution()
    s.islandPerimeter(data)