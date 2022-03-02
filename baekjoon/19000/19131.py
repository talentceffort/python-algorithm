from sys import stdin
# 회의실 예약
stdin = open("19131.txt")

n = int(stdin.readline())

time = sorted([tuple(map(int, stdin.readline().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))

# print(time)

count = last_end_time = 0

for start_time, end_time in time:
    if start_time >= last_end_time:
        count += 1
        last_end_time = end_time

print(count)

# data = []
#
# for _ in range(n):
#     a, b = map(int, stdin.readline().split())
#     data.append((a, b))
#
# print(data)
#
# sorted(data, key=lambda )
