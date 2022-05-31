"""
给你两个长度相同的字符串，s 和 t。

将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。

如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。

输入：s = "abcd", t = "bcdf", maxCost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。

"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = r = 0
        res = 0
        lens = len(s)
        cost = 0

        values = []
        for i in range(lens):
            diff = ord(s[i]) - ord(t[i])
            values.append(diff if diff > 0 else -diff)

        while r < lens:
            cost += values[r]
            while cost > maxCost:
                cost -= values[l]
                l += 1
            if r - l + 1 > res:
                res = r - l + 1
            r += 1

        print(res)
        return res


if __name__ == '__main__':
    s = Solution()
    s.equalSubstring("abcd", "acde", 0)
