import sys

sys.stdin = open("input.txt", "r")

T = int(input())

reward = 0
for _ in range(0, T):
    m, n, k = list(map(int, input().split()))
    if m == n == k:
        money = 10000 + (m * 1000)
    elif m == n or m == k or n == k:
        if m == n or m == k:
            money = 1000 + (m * 100)
        else:
            money = 1000 + (n * 100)
    else:
        max_num = max([m, n, k])
        money = max_num * 100

    if money > reward:
        reward = money

print(reward)