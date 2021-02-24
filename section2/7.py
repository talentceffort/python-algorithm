import sys

sys.stdin = open("input.txt", "r")

n = int(input())

temp = [False, False] + [True] * (n - 1)

prime_number = []

for i in range(2, n + 1):
    if temp[i]:
        prime_number.append(i)
        for j in range(i * 2, n + 1, i):
            temp[j] = False

# print(prime_number)

print(len(prime_number))