import sys

sys.stdin = open("input.txt", "r")

m = int(input())

largest = 0

init = 0

# 강사님이 만든 2차원 배열
T = [list(map(int, input().split())) for _ in range(m)]

array = []

print(T)

for _ in range(m):
    N = list(map(int, input().split()))
    array.append(N)

for k in range(m):
    sum1 = sum2 = 0
    for j in range(m):
        sum1 += array[k][j]
        sum2 += array[j][k]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

for k in range(m):
    sum1 = sum2 = 0
    sum1 += array[k][k]
    sum2 += array[k][m - k - 1]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

print(largest)