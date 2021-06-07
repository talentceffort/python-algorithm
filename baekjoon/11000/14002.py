# 가장 긴 증가하는 부분 수열 4
from sys import stdin

stdin = open("11053.txt")

T = int(stdin.readline())

N = list(map(int, stdin.readline().split()))

dp = [1] * T


for i in range(T):
    for j in range(i):
        if N[i] > N[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = max(dp[j] + 1, dp[i])

order = max(dp)

v = []

for i in range(T - 1 , -1, -1):
    if dp[i] == order:
        v.append(N[i])
        order -= 1

answer = []

v.reverse()

print(max(dp))

for i in v:
    print(i, end=' ')