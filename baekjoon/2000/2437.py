from sys import stdin

stdin = open("2437.txt")

input = stdin.readline

n = input()

data = list(map(int, input().split()))

data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)