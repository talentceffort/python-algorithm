from sys import stdin

stdin = open("6064.txt")

n = int(stdin.readline())

# M, N <= 40000

for x in range(n):
   M, N, x, y = map(int, stdin.readline().split())

   # 나머지 연산을 사용하기 위해 -1
   x = x - 1
   y = y - 1

   k = x

   ok = False

   for i in range(k, M * N, M):
       # y 만 비교하면 됨.
       if i % N == y:
           print(i + 1)
           ok = True
           break

   if ok == False:
       print(-1)








# <10:12>