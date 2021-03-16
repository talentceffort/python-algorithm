import sys

sys.stdin = open("input.txt", "r")

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

x = list(range(21))

for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b - a + 1) // 2):
        x[a + i], x[b - i] = x[b - i], x[a + i]

x.pop(0)

for _ in x:
    print(_, end=" ")
