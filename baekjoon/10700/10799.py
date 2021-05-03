import sys

sys.stdin = open("10799.txt")

T = sys.stdin.readline()

stack = []

index = 0

count = 0

for x in T:
    if x == "(":
        stack.append(index)
    if x == ")":
        n = stack[-1]
        if index - n == 1:
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
    index += 1

print(count)