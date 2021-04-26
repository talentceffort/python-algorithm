import sys

sys.stdin = open("1406.txt")

l_stack = list(sys.stdin.readline().strip())
r_stack = []

N = int(sys.stdin.readline())

for x in range(N):
    aStr = sys.stdin.readline()

    if aStr[0] == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    elif aStr[0] == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    elif aStr[0] == 'B' and l_stack:
        l_stack.pop()
    elif aStr[0] == 'P':
        l_stack.append(aStr[2])

while r_stack:
    l_stack.append(r_stack.pop())

for x in l_stack:
    print(x, end="")
