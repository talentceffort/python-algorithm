from sys import stdin

stdin = open("9095.txt")

n = int(stdin.readline())

print(n)

def go(sum, goal):
    if sum > goal:
        return 0
    if sum == goal:
        return 1

    now = 0

    for i in range(1, 4):
        now += go(sum + i, goal)

    return now


for x in range(n):
    k = int(stdin.readline())

    print(go(0, k))

