def solution(n, lost, reserve):

    s = set(lost) & set(reserve) # 교집합
    l = set(lost) - s # 차집
    r = set(reserve) - s # 차집합

    print(s, l , r)

    for i in sorted(r):
        if i - 1 in l:
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)
    return n - len(l)


print(solution(5, [1, 7], [1, 3]))