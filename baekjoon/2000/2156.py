from sys import stdin

stdin = open("2156.txt")

N = int(stdin.readline())

a = [0] * 10000

for i in range(N):
    a[i] = (int(stdin.readline()))

dp = [0] * 10000


dp[0] = a[0]
dp[1] = a[0] + a[1]
dp[2] = max(a[0] + a[2], a[1] + a[2], dp[1])

for i in range(3, N):
    dp[i] = max(dp[i - 2] + a[i], a[i - 1] + a[i] + dp[i - 3], dp[i - 1])

print(max(dp))