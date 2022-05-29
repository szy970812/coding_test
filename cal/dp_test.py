numbers = [3, 34, 4, 12, 5, 2]


def dp(nums, sum_res):

    dp_map = [[None for _j in range(sum_res + 1)] for _i in range(len(nums))]
    for j in range(sum_res + 1):
        if nums[0] == j:
            dp_map[0][j] = True
        else:
            dp_map[0][j] = False
    for i in range(len(nums)):
        dp_map[i][0] = True
    for ii in range(1, len(nums)):
        for jj in range(1, sum_res + 1):
            if jj < nums[ii]:
                dp_map[ii][jj] = dp_map[ii - 1][jj]
            else:
                chose = dp_map[ii - 1][jj - nums[ii]]
                not_chose = dp_map[ii - 1][jj]
                dp_map[ii][jj] = chose or not_chose

    # for item in dp_map:
    #     print(item)
    return dp_map[-1][-1]


if __name__ == '__main__':
    print(dp(numbers, 9))
    print(dp(numbers, 10))
    print(dp(numbers, 11))
    print(dp(numbers, 36))
    print(dp(numbers, 37))
    print(dp(numbers, 66))
