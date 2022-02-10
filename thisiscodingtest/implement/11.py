from sys import stdin

stdin = open("11.txt")

n = int(stdin.readline())

k = int(stdin.readline())

data = [[0] * (n + 1) for _ in range((n + 1))]
info = []

for _ in range(k):
    a, b = map(int, stdin.readline().split())
    # 사과가 있는 곳은 1 로 표시.
    data[a][b] = 1

l = int(stdin.readline())

for _ in range(l):
    a, b = stdin.readline().split()
    info.append((int(a), b))

# 처음에는 오른쪽을 보고 시작함.(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 0 -> 3, 1 -> 0, 2 -> 1, 3 -> 2
# 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 0
def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    if c == "D":
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1  # 시작 위치
    data[x][y] = 2  # 존재 위치
    direction = 0
    time = 0  # 시작한 뒤에 지난 '초' 시간
    index = 0  # 다음에 회전할 정보
    q = [(x, y)]  # 뱀이 차지 하고 있는 위치 정보(꼬리가 앞)

    while True:
        nx, ny = x + dx[direction], y + dy[direction]

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치면
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거.
            if data[nx][ny] == 0:
                data[nx][ny] = 2  # 위치 수정
                q.append((nx, ny))  # 새로운 꼬리 위치 정보 추가.
                px, py = q.pop(0)  # 큐에서 이전 꼬리 위치 삭제.
                data[px][py] = 0  # 기존 위치 정보 초기화
            # 사과가 있다면 이동 후 꼬리 그대로 두기.
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))  # 사과가 있던 자리엔 꼬리가 생겨야 하므로 위치 정보에 추가.
        # 벽이나 몸통에 부딪침.
        else:
            time += 1
            break

        # 다음 위치로 머리 이동.
        x, y = nx, ny
        time += 1

        # 회전 할 시간이 되면...
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time


print(simulate())
