import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

a = list(map(int, input().split()))

lt = 0

rt = 1

total = a[0]

cnt = 0

# lt 와 rt 를 옮겨주면서 lt 와 rt 사이의 값을 계속 비교.

while True:
    if total < m:
        if rt < n:
            total += a[rt]
            rt += 1
        else:
            break
    elif total == m:
        cnt += 1
        total -= a[lt]
        lt += 1
    else:
        total -= a[lt]
        lt += 1

print(cnt)