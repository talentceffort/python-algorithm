from sys import stdin

stdin = open("11054.txt")

N = int(stdin.readline())

a = list(map(int, stdin.readline().split()))

dp = [1] * N
dp2 = [1] * N

reverse_a = a[::-1]


for i in range(N):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

        if reverse_a[i] > reverse_a[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

ans = 0

result = [0 for i in range(N)]
for i in range(N):
    result[i] = dp[i] + dp2[N - i - 1] - 1

print(max(result))