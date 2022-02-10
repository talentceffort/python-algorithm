from sys import stdin

stdin = open("18406.txt")

# input = stdin.readline

n = list(map(int, input()))

pivot = len(n) // 2

total = 0

for i in range(pivot):
    total += n[i]

for i in range(pivot, len(n)):
    total -= n[i]

if total == 0:
    print('LUCKY')
else:
    print('READY')