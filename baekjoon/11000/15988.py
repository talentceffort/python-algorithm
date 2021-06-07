import sys

sys.stdin = open("15988.txt")

T = int(sys.stdin.readline())

# dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]
# dp[0] = 1 => 0 이 존재하므로 1개 존재

dp = [0 for i in range(12)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for x in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])
