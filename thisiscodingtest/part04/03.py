from sys import stdin

stdin = open("03.txt")

input = stdin.readline

n = input()

# ord 는 문자를 유니코드로 변환.
column = int(ord(n[0]) - int(ord('a'))) + 1

x, y = int(n[1]), column

dx = [-2, -2, 2, 2, 1, -1, 1, -1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

# 나이트가 움직일 수 있는 방향
# 수평으로 두칸 후 수직으로 한 칸 -> 좌 좌 위, 좌 좌 아래, 우 우 위, 우 우 아래
# 수직으로 두 칸 후 수평으로 한 칸 -> 위 위 우, 위 위 좌, 아래 아래 우, 아래 아래 좌

count = 0
for i in range(len(dx)):
    nx = 0
    ny = 0

    nx += x + dx[i]
    ny += y + dy[i]

    if nx < 1 or ny < 1 or nx > len(dx) or ny > len(dx):
        continue
    count += 1

print(count)

row = int(n[1])
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
