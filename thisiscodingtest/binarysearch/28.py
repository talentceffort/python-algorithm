from sys import stdin

stdin = open("28.txt")

input = stdin.readline

n = int(input())

data = list(map(int, input().split()))


def binary_search(array, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if mid == array[mid]:
        return array[mid]

    if mid > array[mid]:
        return binary_search(array, mid + 1, end)
    if mid < array[mid]:
        return binary_search(array, start, mid - 1)


flag = binary_search(data, 0, n - 1)

if flag == 0:
    print(-1)
else:
    print(flag)
