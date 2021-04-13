import sys

sys.stdin = open("input.txt", "r")

T = input()

a = [list(map(int, input().split())) for _ in range(9)]

# print(T)
# print(a)