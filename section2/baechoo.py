import sys

testCount = 0
for n in map(int, sys.stdin.read().split()):
    print(n)



    # (4, 2) => (4, 1), (4, 3), (3, 2), (5, 2)
    # (N, M) => (N, M - 1), (N, M + 1), (N - 1, M), (N + 1, M)
