"""
在给定的二维二进制数组A中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）

现在，我们可以将0变为1，以使两座岛连接起来，变成一座岛。

返回必须翻转的0 的最小数目。（可以保证答案至少是 1 。）

"""
from typing import List


class Solution:
    def __init__(self):
        self.len_i = None
        self.len_j = None
        self.grid = None
        self.source = []
        self.seen = set()
        self.res = 0

    def get_start(self) -> (int, int):
        for i in range(self.len_i):
            for j in range(self.len_j):
                if self.grid[i][j] == 1:
                    return i, j

    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.len_i = len(grid)
        self.len_j = len(grid[0])

        start = self.get_start()
        self.dfs(start)
        self.seen = set(self.source)
        self.bfs()
        print(self.res)
        return self.res

    def bfs(self):
        while self.source:
            lens = len(self.source)
            for num in range(lens):
                i, j = self.source.pop()
                next_site = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
                for r, c in next_site:
                    if r < 0 or c < 0 or r >= self.len_i or c >= self.len_j or (r, c) in self.seen:
                        continue
                    else:
                        if self.grid[r][c] == 0:
                            self.source.insert(0, (r, c))
                            self.seen.add((r, c))
                        elif self.grid[r][c] == 1:
                            return
                        else:
                            continue
            self.res += 1

    def dfs(self, start):
        i, j = start
        if i < 0 or j < 0 or i >= self.len_i or j >= self.len_j or start in self.source or self.grid[i][j] == 0:
            return
        self.grid[i][j] = 2
        self.source.append(start)
        self.dfs((i - 1, j))
        self.dfs((i + 1, j))
        self.dfs((i, j - 1))
        self.dfs((i, j + 1))


if __name__ == '__main__':
    data = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    s = Solution()
    s.shortestBridge(data)
