
import sys

sys.stdin = open("1874.txt")

T = int(sys.stdin.readline())

stack = []
aStr = ''

pivot = 0

found = True

for x in range(T):
    n = int(sys.stdin.readline())
    while n > pivot:
        pivot += 1
        stack.append(pivot)
        aStr += '+'

    if stack[-1] == n:
        stack.pop()
        aStr += '-'
    else:
        found = False

if found == False:
    print("NO")
else:
    for x in aStr:
        print(x)