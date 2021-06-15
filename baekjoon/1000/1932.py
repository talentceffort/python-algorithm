from sys import stdin

stdin = open("1932.txt")

N = int(stdin.readline())

# dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + a[i][j]

a = [0] * N
dp = [0] * N

for x in range(N):
    a[x] = (list(map(int, (stdin.readline().split()))))
    dp[x] = a[x]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + a[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + a[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + a[i][j]


print(max(dp[N - 1]))