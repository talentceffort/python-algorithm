from sys import stdin
from collections import deque, Counter
from functools import reduce

stdin = open("2667.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(stdin.readline())

print(n)

group = [[0] * n for _ in range(n)]
cnt = 0


def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    group[x][y] = cnt

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx, ny))
                    group[nx][ny] = cnt


for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)
