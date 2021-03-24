import sys

sys.stdin = open("input.txt", "r")

T = int(input())

M = [list(map(int, input().split())) for _ in range(T)]

total = 0

# 강사님 풀이
s = e = T // 2
for i in range(T):
    for j in range(s, e + 1):
        total += M[i][j]

    if i < T // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

# 내 풀이
# for K in range(T):
#     print(M[K])

#     if T // 2 - K > -1:
#         for a in range((T // 2) - K, (T // 2) + K + 1, 1):
#             total += M[K][a]
#     else:
#         for a in range(K - (T // 2), T - (K - (T // 2)), 1):
#             total += M[K][a]

print(total)