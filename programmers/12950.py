def solution(arr1, arr2):
    answer = []

    for a, b in zip(arr1, arr2):
        length = len(a)
        result = []
        for x in range(length):
            result.append(a[x] + b[x])
            if x == length - 1:
                answer.append(result)

    print(result)

    return answer


# 2차원 행렬 더하기.
def sumMatrix(A, B):
    for x in zip(A, B):
        return [list(map(sum, zip(*x))) for x in zip(A, B)]


# print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
