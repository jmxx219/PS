# 쉬운 계단 수
from sys import stdin


def solve(n: int):
    dp = [[0] * 10 for __ in range(n + 1)]
    dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][1]
            elif j == 9:
                dp[i][j] = dp[i - 1][8]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    # for x in dp:
    #     print(x)
    return sum(dp[n]) % 1000000000


print(solve(int(stdin.readline())))