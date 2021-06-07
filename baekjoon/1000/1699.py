from sys import stdin

stdin = open("1699.txt")

N = int(stdin.readline())

dp = [0] * (N + 1)

for x in range(1, N + 1):
    dp[x] = x
    for j in range(1, x):
        if j * j > x:
            break
        dp[x] = min(dp[x - j * j] + 1, dp[x])

print(dp[N])

