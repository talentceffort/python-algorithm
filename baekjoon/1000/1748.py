from sys import stdin

stdin = open("1748.txt")

n = int(stdin.readline())

length = len(str(n))

ans = 0

for i in range(1, length):
    ans += i * (pow(10, i) - pow(10, i - 1))

ans += length * (n - pow(10, length - 1) + 1)

print(ans)

