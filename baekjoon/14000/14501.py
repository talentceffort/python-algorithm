from sys import stdin

stdin = open("14501.txt")

N = int(stdin.readline())

T = [0]
P = [0]

for x in range(N):
    a, b = map(int, stdin.readline().split())
    T.append(a)
    P.append(b)


global ans

ans = 0

def go(day, total):
    # 정답을 찾은 경우 => day == N + 1
    # 불가능 한 경우 => day > N + 1
    # 지속 가능 한 경우 => 상담을 하는 경우, 상담을 하지 않는 경우
    # 상담을 한다 => go(day + T[day], sum + P[day])
    # 상담을 하지 않는다 => go(day + 1, sum)

    global ans

    if day == N + 1:
        if ans < total:
            ans = total
        return total

    if day > N + 1:
        return

    go(day + 1, total)
    go(day + T[day], total + P[day])

go(1, 0)

print(ans)