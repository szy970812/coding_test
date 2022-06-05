"""
给你一个整数数组 arr 和两个整数 k 和 threshold 。

请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
"""
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        lens = len(arr)

        average = sum(arr[: k]) / k
        if average >= threshold:
            res += 1

        for i in range(1, lens - k + 1):
            average = average + (arr[i + k - 1] - arr[i - 1]) / k
            if average >= threshold:
                res += 1
        print(res)
        return res


if __name__ == '__main__':
    s = Solution()
    a = [11,13,17,23,29,31,7,5,2,3]
    b = 3
    c = 5
    s.numOfSubarrays(a, b, c)
