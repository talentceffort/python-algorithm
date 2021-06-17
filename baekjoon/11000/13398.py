from sys import stdin

stdin = open("13398.txt")

N = int(stdin.readline())

a = list(map(int, stdin.readline().split()))

dp = [[0, 0] for x in range(N)]

dp[0][0] = a[0]

ans = -1001

if N > 1:
    for i in range(1, N):
        dp[i][0] = max(dp[i - 1][0] + a[i], a[i])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + a[i])

        ans = max(ans, dp[i][0], dp[i][1])

    print(ans)
else:
    print(dp[0][0])


