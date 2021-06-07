from sys import stdin

stdin = open("1149.txt")

N = int(stdin.readline())

# dp[i][j] = i 번째 집 j 로 칠했을 때 , 1 ~ i 번째 집 칠하는 비용의 최소값

# dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + A[i][j]

dp = [[0] * 3 for _ in range(N + 1)]

array = []

for i in range(N):
    array.append(list(map(int, stdin.readline().split())))

dp[1][0] = array[0][0]
dp[1][1] = array[0][1]
dp[1][2] = array[0][2]


for i in range(1, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + array[i - 1][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + array[i - 1][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + array[i - 1][2]

print(min(dp[N]))
