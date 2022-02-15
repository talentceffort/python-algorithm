# 기둥과 보 설치
# [x, y, a, b] -> [가로좌표, 세로좌표, 구조물 종류, 설치 혹은 삭제]
# 0 = 기둥, 1 = 보
# 0 = 삭제, 1 = 설치
# 벽면 벗어나게 기둥, 보 X
# 바닥에 보 설치 X

# 리턴 형식 [x, y, a] x, y 는 기둥, 보의 교차점. [가로 좌표, 세로 좌표] a는 구조물 종류
# 리턴 하는 배열은 x 좌표 기준 오름차순, x 좌표가 같을 경우 y 좌표 기준으로 정렬
# x, y 좌표가 모두 같을 경우 기둥이 보보다 앞에 오면 됨.

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥일 때
            # 맨 바닥, 보의 한쪽 끝 부분 위(끝과 시작), 혹은 다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:  # 보
            # 한쪽 끝 부분이 기둥 위 혹은 양쪽 끝 부분이 다른 보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operator = frame
        if operator == 0:  # 삭제
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operator == 1:  # 설치
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)


# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.


# print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
# [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
