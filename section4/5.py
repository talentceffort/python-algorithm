import sys

sys.stdin = open("section4/5.txt", "r")

T = int(input())

print(T)

meet = []

for _ in range(T):
    s, e = map(int, input().split())
    meet.append((s, e))


meet.sort(key=lambda x: (x[1], x[0]))

pivot = 0
count = 0

for s, e in meet:
    if s >= pivot:
        pivot = e
        count += 1

print(count)
# print(meet)