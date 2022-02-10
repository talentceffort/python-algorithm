from sys import stdin

stdin = open("04.txt")

input = stdin.readline

n, m = map(int, input().split())

x, y, direction = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 처음 시작하는 곳은 방문 처리.
d[x][y] = 1

array = []

for i in range(n):
    array.append(list(map(int, input().split())))


# print(array)
# print(d)
# print(direction)

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
