"""
给你一个整数数组 nums 和一个整数k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

子数组大小 至少为 2 ，且
子数组元素总和为 k 的倍数。
如果存在，返回 true ；否则，返回 false 。

如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        num_dict = {0: [-1]}

        s = 0
        for i, num in enumerate(nums):
            s += num
            d = s % k
            if d not in num_dict:
                num_dict[d] = [i]
            else:
                num_dict[d].append(i)
                if max(num_dict[d]) - min(num_dict[d]) >= 2:
                    return True
        return False


if __name__ == '__main__':
    a = [0, 0]
    b = 17
    s = Solution()
    print(s.checkSubarraySum(a, b))
