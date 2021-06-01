import sys

sys.stdin = open("16194.txt")

T = int(sys.stdin.readline())

prices = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] + ([-1] * T)

print(dp)

for i in range(1, T + 1):
    for j in range(1, i + 1):
        if dp[i] == -1 or dp[i] > dp[i - j] + prices[j]:
            dp[i] = dp[i - j] + prices[j]

print(dp[T])