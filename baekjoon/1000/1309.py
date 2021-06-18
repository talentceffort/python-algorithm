from sys import stdin

stdin = open("1149.txt")

N = int(stdin.readline())

dp = [[0] * 3 for _ in range(N + 1)]

dp[0] = [1, 1, 1]

for i in range(1, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[N - 1]))

# 2차원이 아닌 1차원으로 풀이
# D[i] 는 i 번째에 동물이 있는 경우를 말함.
# D[i] = D[i - 1] + 2(D[i - 2] + ... + D[2] + D[1]
# S[i] = D[1] + D[2] + D[3] + ... + D[i] 를 저장...
# D[i] = D[i - 1] + 2 * S[i - 2] 로 구현 가능.
# 정답은 S[N] 에 존재함.

d = [0 for _ in range(N + 1)]
s = [0 for _ in range(N + 1)]

d[0] = 1 # 안놓는 경우도 1개의 경우의 수가 있음.
s[0] = 1
d[1] = 2
s[1] = d[0] + d[1]

for i in range(2, N + 1):
    d[i] = d[i - 1] + 2 * s[i - 2]
    s[i] = s[i - 1] + d[i]
    d[i] = d[i] % 9901
    s[i] = s[i] % 9901

print(s[N])