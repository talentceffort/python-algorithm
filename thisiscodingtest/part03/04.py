# 1이 될 때까지
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

from sys import stdin

stdin = open("04.txt")

input = stdin.readline

n, k = map(int, input().split())

# 19, 5 -> ?.
# 25, 5 -> 2
result = 0

while True:
    # N이 K로 나누어떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막 남은수에 대하여 1씩 빼기.
result += (n - 1)
print(result)
