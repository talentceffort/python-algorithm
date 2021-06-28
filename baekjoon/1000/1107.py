from sys import stdin

stdin = open("1107.txt")

N = int(stdin.readline())

M = int(stdin.readline())

broken = []

if M > 0:
    broken = list(stdin.readline().split())

print(broken)

def posibble(c):
    c = list(str(c))
    for i in c:
        if i in broken:
            return False
    return True


# 버튼을 아예 누르지 않는 경우를 초기값으로 설정
ans = abs(N - 100)
print(ans)
# 1000001
for i in range(1000001):
    if posibble(i):
        ans = min(ans, len(str(i)) + abs(i - N))

print(ans)

