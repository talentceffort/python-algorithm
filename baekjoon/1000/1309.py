from sys import stdin

stdin = open("1149.txt")

N = int(stdin.readline())

dp = [[0] * 3 for _ in range(N + 1)]

dp[0] = [1, 1, 1]

for i in range(1, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901


print(sum(dp[N - 1]))