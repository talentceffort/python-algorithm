from sys import stdin

stdin = open("04.txt")

input = stdin.readline

n = input()

data = list(map(int, input().split()))
data.sort()

print(data)

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

# 1
# 2
# 3
# 1 + 3
# 2 + 3
# 1 + 2 + 3