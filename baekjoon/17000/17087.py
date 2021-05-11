import sys
from math import gcd

sys.stdin = open("17087.txt")

N, S = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

distance_list = []

for x in a:
    distance = S - x
    distance_list.append(abs(distance))


pivot = distance_list[0]

for x in range(N):
    pivot = gcd(pivot, distance_list[x])

print(pivot)