from sys import stdin, stdout

stdin = open("15652.txt")

N, M = map(int, stdin.readline().split())

a = [0 for _ in range(10)] # 결과를 저장 할 배열


def go(index, start, n, m):
    if index == m:
        # 수열 출력
        print(*a[:m])
        return
    for i in range(start, n + 1):
        a[index] = i
        go(index + 1, i, n, m)

go(0, 1, N, M)