answer = 0


def solution(numbers, target):
    global answer

    answer = 0

    dfs(0, numbers, target, 0)

    return answer


def dfs(index, numbers, target, value):
    global answer

    length = len(numbers)

    if index == length and target == value:
        answer += 1
        return

    if index == length:
        return

    dfs(index + 1, numbers, target, numbers[index] + value)
    dfs(index + 1, numbers, target, -numbers[index] + value)


print(solution([1, 1, 1, 1, 1], 3))
