from sys import stdin

stdin = open("08.txt")

input = stdin.readline

n = input()

result = []
value = 0

for x in n:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print("".join(result))