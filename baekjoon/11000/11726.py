import sys

sys.stdin = open("11726.txt")

T = int(sys.stdin.readline())


dp = [0, 1, 2]

for i in range(3, T + 1):
    dp.append(dp[i - 1] + dp[i - 2])

print(dp[T] % 10007)