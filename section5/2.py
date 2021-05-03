import sys

sys.stdin = open("section5/2.txt", "r")

N = input()

# n = input()
# n = input()

n = 4

# 1 3 5 7 9

# A = int(input())

A = 5

# 0 1 2 3 4 5 6 7 8

K = (2 * A) - 1

for x in range(A):
    print(" " * x + "*" * ((A * 2) - ((2 * x) + 1)))

for x in range(A - 1, 0, -1):
    print(" " * (x - 1) + "*" * ((A * 2) - ((2 * x) - 1)))

# for x in range(A - 1, 0, -1):
#     print(("*" * x) + " " * ((A * 2) - (2 * x)) + ("*" * x))