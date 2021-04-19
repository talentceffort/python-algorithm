import sys

sys.stdin = open("section4/3.txt", "r")

n, m = map(int, input().split())

T = list(map(int, input().split()))

# 6 5 8 5 6 8 7 6 6 7
# 35


def check(mid):
    total = 0
    count = 1
    for x in T:
        total += x
        if total >= mid:
            count += 1
            total = x
    return count


lt = min(T)
rt = sum(T)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2

    if mid >= max(T) and check(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1


print(res)