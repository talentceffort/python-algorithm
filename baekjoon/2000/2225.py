from sys import stdin

stdin = open("2255.txt")

N, K = map(int, stdin.readline().split())

# 첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.
# 0부터 N 까지의 정수 K 개를 더해서 그 합이 N이 되는 경우의 수
# D[K][N] = D[K - 1][N - L] , 0 <= L <= N

# D[K][N]

dp = [[0] * (N + 1) for _ in range(K + 1)]

mod = 1000000000

dp[0][0] = 1

for i in range(1, K + 1):
    for j in range(N + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        dp[i][j] %= mod

print(dp[K][N])
