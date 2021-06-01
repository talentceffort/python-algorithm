import sys

sys.stdin = open("1463.txt")

T = int(sys.stdin.readline())

d = [0] * (T + 1)
d[1] = 0

for i in range(2, T + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1
    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1

print(d[T])