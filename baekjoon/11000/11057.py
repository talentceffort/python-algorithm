from sys import stdin

stdin = open("11057.txt")

T = int(stdin.readline())

dp = [[0] * 10 for _ in range(T + 1)]

# dp[i][1] = 1

# dp[i][j] = dp[i - 1][k], 0 <= k <= j

for i in range(10):
    dp[1][i] = 1

for i in range(2, T + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]


print(sum(dp[T]) % 10007)