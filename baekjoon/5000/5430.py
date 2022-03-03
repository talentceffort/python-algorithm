from sys import stdin
from collections import deque

stdin = open("5430.txt")

t = int(stdin.readline())

for _ in range(t):
    cmd = stdin.readline().rstrip()
    n = int(stdin.readline())
    array = deque(list((stdin.readline().rstrip()[1:-1].split(','))))

    if n == 0:
        array = []

    reverse_check = False
    error_check = False

    for c in cmd:
        if c == 'R':
            reverse_check = not reverse_check
        if c == 'D':
            if array:
                if reverse_check:
                    array.pop()
                else:
                    array.popleft()
            else:
                print('error')
                error_check = True
                break

    if not error_check:
        if reverse_check:
            array.reverse()
            print("[" + ",".join(array) + "]")
        else:
            print("[" + ",".join(array) + "]")
