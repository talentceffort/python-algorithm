# 처음과 마지막이 이웃이다. => 원이다.
# 원이 아닌 직선으로 답을 구하고 원으로 변경. 그리고 하나를 고정하고 문제를 풀어봄.
# 1번 집의 색상을 미리 고정해놓고 다이나믹 3번 실행.

from sys import stdin

stdin = open("17404.txt")

N = int(stdin.readline())


a = []

for x in range(N):
    a.append(list(map(int, stdin.readline().split())))

dp = [[0, 0, 0] for _ in range(N)]

ans = float('inf')

for k in range(3):
    # 처음 집의 색을 정해주기 위해 나머지 집의 값을 최대로 올려줌.
    for j in range(3):
        if j == k:
            dp[0][j] = a[0][j]
        else:
            dp[0][j] = ans

    for i in range(1, N):
        dp[i][0] = min(dp[i -1][1], dp[i - 1][2]) + a[i][0]
        dp[i][1] = min(dp[i -1][0], dp[i - 1][2]) + a[i][1]
        dp[i][2] = min(dp[i -1][1], dp[i - 1][0]) + a[i][2]

    # N 번째 집과 처음에 칠한 집의 색이 같으면 그냥 넘어가고 그렇지 않다면 그 안에서 가장 작은 값을 구해 저장함.
    for j in range(3):
        if j == k:
            continue
        ans = min(ans, dp[-1][j])

print(ans)