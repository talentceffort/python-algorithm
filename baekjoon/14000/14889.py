from sys import stdin

stdin = open("14889.txt")

N = int(stdin.readline())

s = [list(map(int, stdin.readline().split())) for _ in range(N)]

def go(index, first, second):
    if index == N:
        if len(first) > N // 2:
            return -1

        if len(second) > N // 2:
            return -1

        t1 = 0 # 1 번팀의 능력치
        t2 = 0 # 2 번팀의 능력치

        for p1 in first:
            for p2 in first:
                if p1 == p2:
                    continue
                t1 += s[p1][p2]

        for p1 in second:
            for p2 in second:
                if p1 == p2:
                    continue
                t2 += s[p1][p2]

        diff = abs(t1 - t2)
        return diff

    ans = -1


    t1 = go(index + 1, first + [index], second)

    if ans == -1 or (t1 != - 1 and ans > t1):
        ans = t1

    if first:
        first.pop()

    t2 = go(index + 1, first, second + [index])

    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2

    if second:
        second.pop()

    return ans

print(go(0, [], []))