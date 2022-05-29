
n = 4
bag_v = 5
weight_list= [1, 2, 3, 4]
value_list = [2, 4, 4, 5]


def dp(weights, values, num, volume):
    res = 0
    value_sum = sum(values)
    dp_map = [[None for _j in range(value_sum + 1)] for _i in range(num)]
    for j in range(1, value_sum):
        if j == values[0] and weights[0] <= volume:
            dp_map[0][j] = weights[0]

    for i in range(num):
        dp_map[i][0] = 0

    for ii in range(1, num):
        for jj in range(1, value_sum):
            if values[ii] > jj:
                dp_map[ii][jj] = dp_map[ii - 1][jj]
            elif values[ii] == jj:
                dp_map[ii][jj] = weights[ii]
            else:
                prev_weight = dp_map[ii - 1][jj - values[ii]]
                if prev_weight is not None and prev_weight + weights[ii] <= volume:
                    dp_map[ii][jj] = prev_weight + weights[ii]

            if dp_map[ii][jj] is not None and jj > res:
                res = jj

    head = [str(i) for i in range(value_sum + 1)]
    head.insert(0, "value")
    head.insert(0, "weight")
    head.insert(0, "index")
    for a in head:
        print("%8s" % a, end="")
    print()
    for i, item in enumerate(dp_map):
        item.insert(0, values[i])
        item.insert(0, weights[i])
        item.insert(0, i)
        for b in item:
            print("%8s" % b, end="")
        print()
    return res


if __name__ == '__main__':
    res = dp(weight_list, value_list, n, bag_v)
    print(res)
