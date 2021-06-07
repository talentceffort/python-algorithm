# dp[n][0] = dp[n - 1][1] + dp[n - 1][0]
# dp[n][1] = dp[n - 1][0]

# dp[1][0] = 0
# dp[1][1] = 1

from sys import stdin

stdin = open("2193.txt")

T = int(stdin.readline())

dp = [[0] * 2 for _ in range(T + 1)]

dp[1][0] = 0
dp[1][1] = 1

for x in range(2, T + 1):
    dp[x][0] = dp[x - 1][1] + dp[x - 1][0]
    dp[x][1] = dp[x - 1][0]

print(sum(dp[T]))