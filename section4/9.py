import sys

sys.stdin = open("section4/9.txt", "r")

N = int(input())


a = list(map(int, input().split()))

print(a)

lt = 0
rt = N - 1
res = ""
last = 0
temp = []
while lt <= rt:

    if a[lt] > last:
        temp.append((a[lt], "L"))
    if a[rt] > last:
        temp.append((a[rt], "R"))

    temp.sort()

    if len(temp) == 0:
        break
    else:
        res = res + temp[0][1]
        last = temp[0][0]
        if temp[0][1] == "L":
            lt += 1
        else:
            rt -= 1
    temp.clear()


print(len(res))
print(res)