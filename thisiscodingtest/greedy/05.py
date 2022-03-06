from sys import stdin

stdin = open("05.txt")

n, m = map(int, stdin.readline().split())

data = list(map(int, stdin.readline().split()))

array = [0] * 11

for x in data:
    array[x] += 1


result = 0

for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

