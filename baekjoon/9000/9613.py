import sys

sys.stdin = open("9613.txt")

T = int(sys.stdin.readline())

# 3
# 4 10 20 30 40
# 3 7 5 12
# 3 125 15 25


def getGCD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


for _ in range(T):
    N = list(map(int, sys.stdin.readline().split()))
    length = N.pop(0)
    sum = 0
    for x in range(length):
        for j in range(length):
            if x < j:
                sum += getGCD(N[x], N[j])

    print(sum)