from sys import stdin

stdin = open("15651.txt")

N, M = map(int, stdin.readline().split())

a = [0 for _ in range(10)]

def go(index, n, m):
    print("go(index, n, m) ===> go(", index, n, m, ")")
    if index == m:
        print(*a[:m])
        return

    for i in range(1, n + 1):
        a[index] = i
        print("a[index] ===> ", i)
        go(index + 1, n, m)


go(0, N, M)