# food_times	k	result
# [3, 1, 2]	    5	1
# [2, 1, 1]     5

# heap[k] <= heap[2 * (k + 1)] and heap[k] <= heap[2 * (k + 2)]

import heapq


def solution(food_times, k):
    time = 0
    index = 0

    if sum(food_times) <= k:
        return -1

    q = []

    for i in range(len(food_times)):
        # 튜플로 넣어주기
        heapq.heappush(q, (food_times[i], i + 1))

    # 먹기 위해 사용한 시간
    sum_value = 0

    # 직전에 다 먹은 음식 시간
    previous = 0

    # 남은 음식의 개수
    length = len(food_times)

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 K 를 비교.
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]


print(solution([3, 1, 2], 5))
