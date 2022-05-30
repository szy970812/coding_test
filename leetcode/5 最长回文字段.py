"""
给你一个字符串 s，找到 s 中最长的回文子串。
"""


def func(s):
    lens = len(s)
    if lens == 1:
        return s
    dp_map = [[False for _j in range(lens)] for _i in range(lens)]
    for i in range(lens):
        for j in range(lens):
            if i == j:
                dp_map[i][j] = True
            else:
                if s[i] == s[j]:
                    dp_map[i][j] = True
    res = []
    for k in range(2 * lens):
        current_res = []
        for l in range(k + 1):
            if k - l > lens - 1 or l > lens - 1:
                continue
            if dp_map[k - l][l] is True:
                current_res.append((k - l, l))

        if len(current_res) >= 1:
            start = 0
            end = -1
            for r in range(1, len(current_res)):
                if current_res[r][0] == current_res[r - 1][0] - 1:
                    pass
                else:
                    end = r - 1
                    if end - start + 1 > len(res) and current_res[start][0] == current_res[end][1]:
                        res.clear()
                        res.extend(current_res[start: end + 1])
                    start = r
            if end == -1:
                end = len(current_res) - 1
                if end - start + 1 > len(res) and current_res[start][0] == current_res[end][1]:
                    res.clear()
                    res.extend(current_res[start: end + 1])
    # print("".join([s[asd[1]] for asd in res]))
    return "".join([s[asd[1]] for asd in res])


if __name__ == '__main__':
    string = "ac"
    func(string)
