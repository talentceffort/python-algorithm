from sys import stdin
from itertools import permutations

stdin = open("10819.txt")

N = int(stdin.readline())

a = list(map(int, stdin.readline().split()))

a.sort()

b = list(permutations(a, N))

max = 0

def go(arr):
    l = len(arr)
    sum = 0
    i = 0

    while i < l - 1:
        sum += abs(arr[i] - arr[i + 1])
        i += 1

    return sum

for x in b:
    x = list(x)
    if max < go(x):
        max = go(x)


print(max)