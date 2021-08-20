from sys import stdin

stdin = open("2529.txt")

n = int(stdin.readline())

print(n)

a = stdin.readline().split()

ans = []

answer = ''

check = [False] * 10

def validation(x, y, op):
    if op == '<':
        if x > y:
            return False

    if op == '>':
        if x < y:
            return False

    return True
def go(index, answer):
    if index == n + 1:
        ans.append(answer)
        return

    for i in range(0, 10):
        if check[i]:
            continue
        if index == 0 or validation(answer[index - 1], str(i), a[index - 1]): # 이전, 현재, 부등호
            check[i] = True
            go(index + 1, answer + str(i))
            check[i] = False

go(0, '')
print(ans[-1])
print(ans[0])
