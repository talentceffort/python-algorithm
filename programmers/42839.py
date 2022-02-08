from itertools import permutations
import math


def is_prime_num(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    numArray = list(map(str, numbers))

    per = []

    for i in range(1, len(numbers) + 1):  # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per += list(permutations(numArray, i))  # i개씩 순열조합

    nums = [int(("").join(p)) for p in per]

    nums = list(set(nums))

    for x in nums:
        data = int(x)
        if is_prime_num(data):
            answer.append(data)
    return len(answer)


print(solution("011"))
