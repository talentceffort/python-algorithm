import sys

sys.stdin = open("11052.txt")

T = int(sys.stdin.readline())

prices = [0] + list(map(int, sys.stdin.readline().split()))

#price = [0] + [int(x) for x in stdin.readline().split()]

dp = prices[:]


# dp[i] = max(dp[i], dp[i - j] + price[j])
# dp[N] = dp[N - i] + price[i]
# dp[1] = dp[0] + price[1]
# dp[4] = dp[0] + price[4]

for i in range(1, T + 1):
    for j in range(1, i + 1):
        dp[i] = (max(dp[i], dp[i - j] + prices[j]))


print(dp)


