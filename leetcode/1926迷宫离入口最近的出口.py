"""
给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始），矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）。同时给你迷宫的入口 entrance ，用 entrance = [entrancerow, entrancecol] 表示你一开始所在格子的行和列。

每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 entrance 最近 的出口。出口 的含义是 maze 边界 上的 空格子。entrance 格子 不算 出口。

请你返回从 entrance 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 -1 。
"""
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        res = 0
        lens_i = len(maze)
        lens_j = len(maze[0])
        queue = list()
        queue.append(tuple(entrance))
        walked = set()

        while queue:
            current_len = len(queue)
            for _ in range(current_len):
                i, j = current_site = queue.pop(0)
                walked.add(current_site)
                print(current_site)
                next_site = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
                for m, n in next_site:
                    if m < 0 or n < 0 or m >= lens_i or n >= lens_j:
                        continue
                    elif m == 0 or n == 0 or m == lens_i - 1 or n == lens_j - 1:
                        if maze[m][n] == "." and (m, n) != tuple(entrance):
                            print(res + 1)
                            return res + 1
                    else:
                        if maze[m][n] == "." and (m, n) not in walked and (m, n) not in queue:
                            queue.append((m, n))

            res += 1
        print(-1)
        return -1


if __name__ == '__main__':
    s = Solution()
    a = [["+", ".", "+", "+", "+", "+", "+"],
         ["+", ".", "+", ".", ".", ".", "+"],
         ["+", ".", "+", ".", "+", ".", "+"],
         ["+", ".", ".", ".", "+", ".", "+"],
         ["+", "+", "+", "+", "+", ".", "+"]]
    b = [0, 1]
    s.nearestExit(a, b)
