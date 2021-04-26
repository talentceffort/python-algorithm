import sys

sys.stdin = open("9093.txt")


n = int(input())


for i in range(n):
    li = input().split()

    for s in li:
        print(s[::-1], end=' ')
    print()

