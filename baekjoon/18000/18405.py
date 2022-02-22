from sys import stdin
from collections import deque

stdin = open("18405.txt")

n, k = map(int, stdin.readline().split())

graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
data = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

target_s, target_x, target_y = map(int, stdin.readline().split())

data.sort()
q = deque(data)

while q:
    virus, s, x, y = q.popleft()

    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
