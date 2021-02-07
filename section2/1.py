def measure(p, q):
    mea = []
    for num in range(1, p):
        if p % num == 0:
            mea.append(num)
    if len(mea) < q:
        return -1
    return mea[q - 1]


print(measure(6, 3))


# 개선
def measure2(p, q):
    cnt = 0
    for i in range(1, p + 1):
        if (p % i == 0):
            cnt += 1
        if cnt == q:
            return i
            break
    else:
        return -1

print(measure2(6, 3))