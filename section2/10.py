import sys

sys.stdin = open("input.txt", "r")

T = int(input())

a = list(map(int, input().split()))

# 내 풀이
nu = 0
prev = 0
total = 0

for x in range(0, len(a)):
    if x - 1 >= 0 and bool(a[x]):
        if prev == a[x]:
            nu += 1
        else:
            nu = 0
    if bool(a[x]):
        total += 1 + nu
    prev = a[x]

print(total)

# 강의 풀이
sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)
