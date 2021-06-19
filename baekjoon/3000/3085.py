from sys import stdin

stdin = open("3085.txt")

N = int(stdin.readline())

candy = [list(stdin.readline()) for _ in range(N)]

cnt = 0

for i in range(N):
    if N - 1 != i:
        candy[i].pop()

def check(arr):
    result = 1
    for x in range(N):
        cnt = 1
        for j in range(1, N):
            if arr[x][j] == arr[x][j - 1]:
                cnt += 1
            else:
                cnt = 1

            if cnt > result:
                result = cnt

        cnt = 1
        for j in range(1, N):
            if arr[j][x] == arr[j - 1][x]:
                cnt += 1
            else:
                cnt = 1

            if cnt > result:
                result = cnt

    return result

for i in range(N):
    for j in range(N):
        # 오른쪽으로 변경
        if j + 1 < N:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

            temp = check(candy)

            if temp > cnt:
                cnt = temp

            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

        # 아래로 변경
        if i + 1 < N:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

            temp = check(candy)

            if temp > cnt:
                cnt = temp

            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

print(cnt)