import heapq

def solution(scoville, K):
    answer = 0

    temp = []

    for x in scoville:
        heapq.heappush(temp, x)



    while temp[0] <= K:

        if len(temp) == 1:
            return -1

        new_food = heapq.heappop(temp) + (heapq.heappop(temp) * 2)

        heapq.heappush(temp, new_food)

        answer += 1

    return answer



print(solution([1, 2, 3, 9, 10, 12], 7))

# print(solution([1,1,1,1], 12))
