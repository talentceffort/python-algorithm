import sys

sys.stdin = open("1676.txt")

T = int(sys.stdin.readline())

count = 0

for x in range(1, T + 1):
    if x % 5 == 0:
        count += 1
    if x % 25 == 0:
        count += 1
    if x % 125 == 0:
        count +=1

print(count)
