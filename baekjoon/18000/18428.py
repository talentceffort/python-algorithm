from itertools import combinations
from sys import stdin

stdin = open("18428.txt")

n = int(stdin.readline())

board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(stdin.readline().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))


def watch(x, y, direction): # 학생 발견 True, 미발견 False
    # 왼쪽으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    # 오른쪽으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # 위쪽으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    # 아래쪽으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1


def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'

    # 학생이 한명도 감지되지 않았을 때
    if not process():
        print(data)
        find = True
        break

    for x, y in data:
        board[x][y] = 'X'


if find:
    print('YES')
else:
    print('NO')