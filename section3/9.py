import sys

sys.stdin = open("input.txt", "r")

T = int(input())

a = [list(map(int, input().split())) for _ in range(T)]

a.insert(T, [0] * (T + 2))
a.insert(0, [0] * (T + 2))

for x in range(1, T + 1):
    a[x].insert(0, 0)
    a[x].append(0)

count = 0

for x in range(1, T + 1):
    for y in range(1, T + 1):
        if (
            a[x - 1][y] < a[x][y]
            and a[x + 1][y] < a[x][y]
            and a[x][y - 1] < a[x][y]
            and a[x][y + 1] < a[x][y]
        ):
            count += 1

print(count)
# 기준 a[1][1]
# 상 a[0][1] a[x - 1][1]
# 하 a[2][1] a[x + 1][1]
# 좌 a[1][0] a[1][y - 1]
# 우 a[1][2] a[1][y - 1]
