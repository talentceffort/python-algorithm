import sys

sys.stdin = open("section4/7.txt", "r")

L = int(input())

arr = list(map(int, input().split()))

m = int(input())

cnt = [0] * 101

maxH = float("-inf")
minH = float("inf")


for x in arr:
    cnt[x] += 1
    if x > maxH:
        maxH = x
    if x < minH:
        minH = x


print(maxH, minH)


for _ in range(m):
    if cnt[maxH] == 1:
        cnt[maxH] -= 1
        maxH -= 1
        cnt[maxH] += 1
    else:
        cnt[maxH] -= 1
        cnt[maxH - 1] += 1

    if cnt[minH] == 1:
        cnt[minH] -= 1
        minH += 1
        cnt[minH] += 1
    else:
        cnt[minH] -= 1
        cnt[minH + 1] += 1


print(maxH - minH)
