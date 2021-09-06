from sys import stdin

stdin = open("1248.txt")

n = int(stdin.readline())

s = list(map(str, stdin.readline()))

sign = [[0] * n for _ in range(n)]

ans = [0] * n

count = 0

for i in range(n):
    for j in range(i, n):
        if s[count] == 0:
            sign[i][j] = 0
        if s[count] == '+':
            sign[i][j] = 1
        if s[count] == '-':
            sign[i][j] = -1
        count += 1

def validation(index):
    s = 0
    for k in range(index, -1, -1):
        s += ans[k]
        if sign[k][index] == 0:
            if s != 0:
                return False

        if sign[k][index] > 0:
            if s <= 0:
                return False

        if sign[k][index] < 0:
            if s >= 0:
                return False
    return True


def go(index):
    if index == n:
        return True

    if sign[index][index] == 0:
        ans[index] = 0
        return validation(index) and go(index + 1)

    for i in range(1, 11):
        ans[index] = sign[index][index] * i
        if validation(index) and go(index + 1):
            return True

    return False




go(0)

print(*ans)
