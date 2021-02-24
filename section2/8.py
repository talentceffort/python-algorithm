import sys

sys.stdin = open("input.txt", "r")

T = int(input())

a = list(map(int, input().split()))


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


for n in a:
    tmp = reverse(n)
    if isPrime(tmp):
        print(tmp, end=" ")
