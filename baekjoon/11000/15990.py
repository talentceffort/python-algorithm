import sys

sys.stdin = open("15990.txt")

max = 100000

mod = 1000000009

dp = [[0] * 4 for _ in range(11) ]

dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]


for i in range(4, 11):
    dp[i][1] = dp[i - 1][2] + dp[i - 1][3]
    dp[i][2] = dp[i - 2][1] + dp[i - 2][3]
    dp[i][3] = dp[i - 3][1] + dp[i - 3][2]

    dp[i][1] %= mod
    dp[i][2] %= mod
    dp[i][3] %= mod

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    print(sum(dp[N]) % mod)

