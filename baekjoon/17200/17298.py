import sys

sys.stdin = open("17298.txt")

# 9 5 4 8

N = int(sys.stdin.readline())

T = list(map(int, sys.stdin.readline().split()))

oh_big = [-1 for _ in range(N)]

stack = []

for x in range(N):
    while stack and T[stack[-1]] < T[x]:
        oh_big[stack.pop()] = T[x]
    stack.append(x)

print(*oh_big)

