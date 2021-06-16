from sys import stdin

stdin = open("11055.txt")

N = int(stdin.readline())

# print(N)

a = list(map(int, stdin.readline().split()))

dp = a[:]

for i in range(N):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])



print(max(dp))

