from sys import stdin
from itertools import combinations

stdin = open("15686.txt")

input = stdin.readline

n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

chicken = []
house = []

for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            chicken.append((i, j))
        if data[i][j] == 1:
            house.append((i, j))

candidates = list(combinations(chicken, m))


def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result


result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
