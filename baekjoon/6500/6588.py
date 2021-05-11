import sys

sys.stdin = open("6588.txt")

MAX = 1000000

# temp = [False, False] + [True] * (MAX - 1)
temp = [True] * (MAX + 1)

prime = []

count = 0

for x in range(2, MAX + 1):
    if temp[x]:
        prime.append(x)
        count += 1
        for j in range(x * 2, MAX + 1, x):
                temp[j] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for i in range(1, count):
        if temp[n - prime[i]]:
            print(f'{n} = {prime[i]} + {n - prime[i]}')
            break