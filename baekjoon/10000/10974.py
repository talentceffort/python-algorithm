from sys import stdin
import itertools

stdin = open("10974.txt")

N = int(stdin.readline())

a = []

for x in range(1, N + 1):
    a.append(str(x))


b = list(map(''.join, itertools.permutations(a))) #  수열 만들기

for i in b:
    for j in i:
        print(j, end = ' ')
    print()