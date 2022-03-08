from sys import stdin
import heapq

stdin = open("1715.txt")

n = int(stdin.readline())

heap = []

for i in range(n):
    data = int(stdin.readline())
    heapq.heappush(heap, data)

result = 0

if len(heap) == 1:
    print(0)
else:
    while heap:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        if heap:
            heapq.heappush(heap, a + b)

        result += a + b

    print(result)


