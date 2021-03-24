# 첫 번째는 행 번호, 두 번째는 방향 0 이면 왼쪽, 1이면 오른쪽, 세 번째 수는 회전하는 격자의 수

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

a = [list(map(int, input().split())) for _ in range(T)]

m = int(input())


for _ in range(m):
    x, y, z = list(map(int, input().split()))

    if y == 0:
        for _ in range(z):
            # 제일 앞에서 꺼냄
            a[x - 1].append(a[x - 1].pop(0))
    else:
        for _ in range(z):
            # 제일 뒤에서 꺼냄
            a[x - 1].insert(0, a[x - 1].pop())

s = 0
e = T - 1
total = 0

for i in range(T):
    for j in range(s, e + 1):
        total += a[i][j]

    if i < T // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(total)
# 왼쪽으로 1 이동시 [1, 2, 3] => [3, 1, 2] / [-1, 0, 1] /
# 오른쪽으로 1 이동시 [1, 2, 3] => [3, 1, 2]
