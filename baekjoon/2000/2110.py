import os
from sys import stdin

os.chdir('./baekjoon/2000')
stdin = open("2110.txt")

n, c = map(int, (stdin.readline().split()))

array = [int(stdin.readline()) for x in range(n)]

array.sort()

min_gap = 1
max_gap = array[-1] - array[0]
result = 0

while(min_gap <= max_gap):
    gap = (min_gap + max_gap) // 2
    count = 1
    value = array[0]

    for i in range(1, n):
        if array[i] >= value + gap:
            value = array[i]
            count += 1
        
    if count >= c:
        min_gap = gap + 1
        result = gap
    else:
        max_gap = gap - 1


print(result)