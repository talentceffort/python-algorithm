from sys import stdin

stdin = open("11722.txt")

N = int(stdin.readline())

a = list(map(int, stdin.readline().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))