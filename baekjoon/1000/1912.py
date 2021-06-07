from sys import stdin

stdin = open("1912.txt")

N = int(stdin.readline())

print(N)

array = list(map(int, stdin.readline().split()))

dp = [0] * N

dp[0] = array[0]

for i in range(1, N):
    dp[i] = max(dp[i - 1] + array[i], array[i])


print(max(dp))