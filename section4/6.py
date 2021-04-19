import sys

sys.stdin = open("section4/6.txt", "r")

T = int(input())

print(T)

player = []

for x in range(T):
    t, w = map(int, input().split())
    player.append((t, w))

player.sort(reverse=True)
# print(player)

pivot = 0
count = 0

for t, w in player:
    if w >= pivot:
        pivot = w
        count += 1


print(count)