import sys

sys.stdin = open("section4/1.txt", "r")

n, m = map(int, input().split())

T = list(map(int, input().split()))

T.sort()

print(T)

lt = 0
rt = n - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if T[mid] == m:
        print(mid + 1)
        break
    elif T[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
