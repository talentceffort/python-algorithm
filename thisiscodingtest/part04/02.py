from sys import stdin

stdin = open("02.txt")

input = stdin.readline

n = int(input())

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
# 03 13 23 33 43 53
