import sys

sys.stdin = open("section4/10.txt", "r")

T = int(input())


# print(T)

N = list(map(int, input().split()))

print("N 값 :", N)

temp = [0] * T

print("Temp 값 :", temp)

for x in range(T):
    pivot = 0
    for j in range(T):
        if N[x] == 0 and temp[j] == 0:
            temp[j] = x + 1
            break
        if temp[j] == 0:
            N[x] -= 1


for x in temp:
    print(x, end=" ")
