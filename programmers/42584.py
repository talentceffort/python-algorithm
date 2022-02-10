from collections import deque


def solution(prices):
    answer = []

    q = deque(prices)

    while q:
        p = q.popleft()
        result = 0
        for price in q:
            if p > price:
                result += 1
                break
            result += 1
        answer.append(result)

    return answer


solution([1, 2, 3, 2, 3])
