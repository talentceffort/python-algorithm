import sys

sys.stdin = open("input.txt", "r")

T = int(input())

a = [list(map(int, input().split())) for _ in range(T)]

a.insert(T, [0] * T)
a.insert(0, [0] * T)

print(a)
