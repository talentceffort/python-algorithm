from sys import stdin

stdin = open("1439.txt")

input = stdin.readline

n = input()

count0 = 0
count1 = 0

if n[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(n) - 1):
    data = int(n[i])

    if n[i] != n[i + 1]:
        if data == 1:
            count0 += 1
        else:
            count1 += 1
    init = data


print(min(count0, count1))
