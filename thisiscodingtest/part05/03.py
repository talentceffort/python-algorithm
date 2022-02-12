# 음료수 얼려 먹기
from sys import stdin

stdin = open("03.txt")

# invalid literal for int() with base 10: '\n' 오류 메시지가 난다면  rstrip()를 붙여 주기

input = stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

print(graph)


def dfs(x, y):
    # 범위를 나갔을 때 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 방문 할 수 있다면!
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True

    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            print(i, j)
            result += 1

print(result)
