"""
给定一个整数数组temperatures，表示每天的温度，返回一个数组answer，其中answer[i]是指在第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用0 来代替。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lens = len(temperatures)
        stack = list()
        result = [0 for _ in range(lens)]
        stack.append((0, temperatures[0]))
        for i in range(1, lens):
            while stack:
                if temperatures[i] > stack[-1][1]:
                    s_index, s_temp = stack.pop()
                    result[s_index] = i - s_index
                else:
                    break
            stack.append((i, temperatures[i]))
        print(result)
        return result


if __name__ == '__main__':
    s = Solution()
    data = [73,74,75,71,69,72,76,73]
    s.dailyTemperatures(data)
