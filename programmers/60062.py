from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    weak = weak + [w + n for w in weak]
    answer = len(dist) + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1  # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1  # 새로운 친구 투입
                    if count > len(dist):  # 더 투입이 불가능 하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer


solution(12, [1, 3, 4, 9, 10], [3, 5, 7])
