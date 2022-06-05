"""
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

如果不存在满足条件的子数组，则返回 0 。


"""
import collections
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        r = l = res = 0
        min_q = collections.deque()
        max_q = collections.deque()
        for num in nums:
            while len(min_q) and num < min_q[-1]:
                min_q.pop()
            while len(max_q) and num > max_q[-1]:
                max_q.pop()
            min_q.append(num)
            max_q.append(num)
            r += 1
            while max_q[0] - min_q[0] > limit:
                if min_q[0] == nums[l]:
                    min_q.popleft()
                if max_q[0] == nums[l]:
                    max_q.popleft()
                l += 1
            res = max(res, r - l)
        print(res)
        return res


if __name__ == '__main__':
    s = Solution()
    a = [10,1,2,4,7,2]
    b = 5
    s.longestSubarray(a, b)
