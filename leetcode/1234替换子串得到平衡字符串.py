"""
有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。

假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。

 

给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。

你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。

请返回待替换子串的最小可能长度。

如果原字符串自身就是一个平衡字符串，则返回 0。

输入：s = "QQWE"
输出：1
解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
"""


class Solution:
    def __init__(self):
        self.total_count = dict()
        self.extra_count = dict()
        self.string = None
        self.lens = None
        self.balance_len = None

    def get_count(self):
        for c in self.string:
            if c in self.total_count:
                self.total_count[c] += 1
            else:
                self.total_count[c] = 1
        for k, v in self.total_count.items():
            if v > self.balance_len:
                self.extra_count[k] = v - self.balance_len

    def check_balance(self, current_count: dict):
        for k, v in self.extra_count.items():
            try:
                if v > current_count[k]:
                    return False
            except KeyError:
                return False
        return True

    def balancedString(self, s: str) -> int:
        self.string = s
        self.lens = len(s)
        self.balance_len = self.lens // 4

        self.get_count()
        if not self.extra_count:
            print(0)
            return 0

        res = list()
        l = r = 0
        current_count = dict()

        while r < self.lens:
            if s[r] in current_count:
                current_count[s[r]] += 1
            else:
                current_count[s[r]] = 1
            while self.check_balance(current_count):
                res.append(r - l + 1)
                current_count[s[l]] -= 1
                l += 1

            r += 1

        print(min(res))
        return min(res)


if __name__ == '__main__':
    s = Solution()
    s.balancedString("WQWRQQQW")