import sys

sys.stdin = open("section4/4.txt", "r")

M, H = map(int, input().split())

# 1 2 4 8 9

k = []
for _ in range(M):
    T = int(input())
    k.append(T)

k.sort()


def check(mid):
    cnt = 1
    pivot = k[0]
    for x in range(1, M):
        if k[x] - pivot >= mid:
            cnt += 1
            pivot = k[x]
    return cnt


lt = 1
rt = k[M - 1] - k[0]

res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid) >= H:
        res = mid
        # 최적화된 해를 찾아야 하므로 작은쪽에서 올린다.
        lt = mid + 1
    else:
        rt = mid - 1

print(res)