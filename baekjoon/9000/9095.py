import sys

sys.stdin = open("9095.txt")

T = int(sys.stdin.readline())


# dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]
# dp[0] = 1 => 0 이 존재하므로 1개 존재

for x in range(T):
    N = int(sys.stdin.readline())

    dp = [1, 1, 2]

    for i in range(3, N + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    print(dp[N])

    dp.clear()



