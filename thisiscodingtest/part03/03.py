from sys import stdin

stdin = open("03.txt")

input = stdin.readline

# int(stdin.readline())

n, m = map(int, input().split())

result = 0

for x in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    # if min_value > result:
    #     result = min_value

    result = max(result, min_value)

print(result)