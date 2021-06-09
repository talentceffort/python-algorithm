from sys import stdin

stdin = open("9465.txt")

T = int(stdin.readline())


for _ in range(T):
    n = int(stdin.readline())

    dp = [[0] * 3 for _ in range(n + 1)]

    a = [list(map(int, stdin.readline().split())) for _ in range(2)]


    # 0 은 뜯지 않음
    # 1 은 위쪽 스티커 뜯음
    # 2 는 아래 스티커 뜯음

    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + a[0][i - 1]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + a[1][i - 1]

    print(max(dp[n]))


