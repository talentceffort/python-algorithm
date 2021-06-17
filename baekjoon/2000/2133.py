from sys import stdin

stdin = open("2133.txt")

N = int(stdin.readline())

if N % 2 != 0:
    print(0)
else:
    dp = [0 for _ in range(N + 1)]

    dp[0], dp[2] = 1, 3

    for i in range(4, N + 1):
        dp[i] = dp[i - 2] * 3
        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2

    print(dp[N])

