# 1 2 3 4 5 / 1 2 3 4 5 / 1 2 3 4 5  -5 개
# 2 1 2 3 2 4 2 5 / 2 1 2 3 2 4 2 5 - 8 개
# 3 3 1 1 2 2 4 4 5 5 / 3 3 1 1 2 2 4 4 5 5 - 10

# enumerate 개념 중요.
# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    answer = []

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    c1 = 0
    c2 = 0
    c3 = 0

    for x in range(len(answers)):
        if answers[x] == supo1[x % len(supo1)]:
            c1 += 1
        if answers[x] == supo2[x % len(supo2)]:
            c2 += 1
        if answers[x] == supo3[x % len(supo3)]:
            c3 += 1

    temp = [c1, c2, c3]

    for index, value in enumerate(temp):
        if value == max(temp):
            answer.append(index + 1)

    return answer