# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# (1 ≤ M ≤ N ≤ 8)

from sys import stdin, stdout

stdin = open("15649.txt")

N, M = map(int, stdin.readline().split())

a = [0 for _ in range(10)] # 결과를 저장 할 배열

# N 과 M 에서 선택방식으로 2^N 의 시간복잡도를 가짐. 이 방식이 N 과 M 에서의 핵심.

def go(index, selected, n, m):
    if selected == m:
        # stdout.write(' '.join(map(str,a))+'\n')
        print(*a[:m])
        return
    if index > n:
        return
    a[selected] = index
    go(index + 1, selected + 1, n, m) # index 의 결과에 추가
    a[selected] = 0
    go(index + 1, selected, n, m) # index 를 결과에 추가 하지 않음

go(1, 0, N, M)

# def go(index, start, n, m):
#     if index == m:
#         # 수열 출력
#         print(*a[:m])
#         return
#     for i in range(start, n + 1):
#         a[index] = i
#         go(index + 1, i + 1, n, m)
#
# go(0, 1, N, M)

