# 가장  증가하는 부분 수열 LIS

# 이것도 dp 로...?

# D[i] = A[1] ... A[i]

# D[i] = max(D[j]) + 1, j < i, A[j] < A[i]

from sys import stdin

stdin = open("11053.txt")

T = int(stdin.readline())


N = list(map(int, stdin.readline().split()))

dp = [1] * T

for i in range(T):
    for j in range(i):
        if N[i] > N[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))