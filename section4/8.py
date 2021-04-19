import sys

sys.stdin = open("section4/8.txt", "r")

m, n = map(int, input().split())


h = list(map(int, input().split()))


h.sort(reverse=True)

count = 0
lt = 0
rt = m - 1

while lt <= rt:
    if h[lt] + h[rt] <= n:
        count += 1
        lt += 1
        rt -= 1
    else:
        count += 1
        lt += 1

print(count)

# 아래는 강사님 풀이

# while h:
#   if h[0] + h[-1] > n:
#     h.pop()
#     count += 1
#   else:
#     h.pop(0)
#     h.pop()
#     count += 1