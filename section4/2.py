import sys

sys.stdin = open("section4/2.txt", "r")


def Count(len):
    cnt = 0
    for x in Line:
        cnt += x // len
        return cnt


n, m = map(int, input().split())

Line = []

res = 0

largest = 0

for _ in range(n):
    a = int(input())
    Line.append(a)
    largest = max(largest, a)


lt = 1
rt = largest

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)