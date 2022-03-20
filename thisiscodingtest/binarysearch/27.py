from bisect import bisect_left, bisect_right
from sys import stdin

stdin = open("27.txt")

input = stdin.readline

n, x = map(int, input().split())

data = list(map(int, input().split()))

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


count = count_by_range(data, x, x)

if count == 0:
    print(-1)
else:
    print(count)