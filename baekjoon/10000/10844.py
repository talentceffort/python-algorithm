# dp[N][L] = 길이가 N 이고 마지막 수가 L 인 계단

# dp[N][L] = dp[N - 1][L + 1] + dp[N - 1][L + 1]

from sys import stdin


stdin = open("10844.txt")

T = int(stdin.readline())


dp = [[0] * 10 for _ in range(T + 1)]

for x in range(1, 10):
    dp[1][x] = 1

for x in range(2, T + 1):
   dp[x][0] = dp[x - 1][1]
   dp[x][9] = dp[x - 1][8]

   for j in range(1, 9):
       dp[x][j] = dp[x - 1][j + 1] + dp[x - 1][j - 1]

print(sum(dp[T]) % 1000000000)