import sys

sys.stdin = open("2960.txt")

M, N = map(int, sys.stdin.readline().split())

check = [False] * (M + 1)

count = 0


for i in range(2, M + 1):
    if check[i] == False:
        for j in range(i, M + 1, i):
            if check[j] == False:
                check[j] = True
                count+=1


            if count == N:
                print(j)
                break

