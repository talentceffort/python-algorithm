import sys

sys.stdin = open("section4/7.txt", "r")

T = int(input())


a = list(map(int, input().split()))

S = int(input())


a.sort()


for x in range(S):
    a[T - 1] -= 1
    a[0] += 1
    a.sort()


print(a[T - 1] - a[0])
