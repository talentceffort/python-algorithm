from sys import stdin

stdin = open("14502.txt")

n, m = map(int, stdin.readline().split())

data = [list(map(int, stdin.readline().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

print(data)
print(temp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


def move_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                move_virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1

    return score


def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    move_virus(i, j)

        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                print(i, j, data)
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)
