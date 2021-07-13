from sys import stdin
from itertools import permutations

stdin = open("10971.txt")

N = int(stdin.readline())

W = []

num = []

for x in range(N):
    W.append(list(map(int, stdin.readline().split())))
    num.append(x)

a = list(permutations(num, N))

ans = 2147483647

def go(arr):
    acc = 0

    flag = True

    global ans

    for x in range(N - 1):
        if W[arr[x]][arr[x + 1]] == 0:
            flag = False
            break
        else:
            acc += W[arr[x]][arr[x + 1]]

    if flag and W[arr[N - 1]][arr[0]] != 0:
        acc += W[arr[N - 1]][arr[0]]
        ans = min(acc, ans)

    if flag:
        return acc
    else:
        return 2147483648



for x in a:
    go(list(x))

print(ans)