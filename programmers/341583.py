# def solution(priorities, location):
#     answer = 0
#
#     queue = [(i, p) for i, p in enumerate(priorities)]
#
#     while True:
#         cur = queue.pop(0)
#         # print(queue)
#         # if cur[1] < max(queue, key=lambda x: x[1])[1]:
#         #     queue.append(cur)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer


# print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))

# [2, 1, 3, 2] -> [1, 3, 2, 2] -> [1, 2, 2]


def solution(citations):
    citations.sort(reverse=True)

    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx

    return len(citations)

# [6, 5, 3, 1, 0]
print(solution([3, 0, 6, 1, 5]))
