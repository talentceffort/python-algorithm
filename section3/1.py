import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    a = list(map(str, input().split()))

    word = a[0].upper()
    size = len(word)

    # print("word", word[::-1]) 리버스 해주는 것 => [::-1] 파이썬스럽게.

    for a in range(0, size // 2):
        if word[a] != word[len(word) - a - 1]:
            print("#%d NO" % (_ + 1))
            break
    else:
        print("#%d YES" % (_ + 1))

    # 다른 방법

    # if word == word[::-1]:
    #     print("#%d YES" % (_ + 1))
    # else:
    #     print("#%d NO" % (_ + 1))
