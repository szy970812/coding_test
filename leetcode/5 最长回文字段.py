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
    res = [s[0]]
    res_index = [0]
    max_len = 1
    for k in range(2 * lens):
        flag = False
        current_res = []
        current_index = []
        current_lens = 0
        for l in range(k + 1):
            if k - l > lens - 1 or l > lens - 1:
                continue
            if dp_map[k - l][l] is True:
                if k == 4:
                    print((k - l, l))
                flag = True
                current_lens += 1
                current_res.append(s[l])
                current_index.append(l)
            if flag and (dp_map[k - l][l] is False or k == l or l == lens - 1):
                if current_lens >= max_len:
                    max_len = current_lens
                    res.clear()
                    res.extend(current_res)
                    res_index.clear()
                    res_index.extend(current_index)
                break

    print("".join(res))
    print(res_index)


if __name__ == '__main__':
    string = "aacabdkacaa"
    func(string)
