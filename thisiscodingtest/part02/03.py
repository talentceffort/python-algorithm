from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

print(n, m)

for x in range(n):
    print(input())