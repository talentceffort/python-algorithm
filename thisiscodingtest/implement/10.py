# 자물쇠 90도 회전 시키는 함수
def rotate_a_matrix_by_90_degree(a):
    # n = len(a)
    # m = len(a[0])
    # result = [[0] * n for _ in range(m)]
    # for i in range(n):
    #     for j in range(m):
    #         result[j][n - i - 1] = a[i][j]
    # return result
    return list(zip(*a[::-1]))


# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    # 기존보다 3배 크기로 만들어 줬으니 3으로 나눔.
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


# 자물쇠와 열쇠
def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # print(key)

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        # 열쇠 회전
        key = rotate_a_matrix_by_90_degree(key)
        # print(key)
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠의 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        # 9개의 값을 변경해야 하므로...
                        # 0 ~ 7 까지만 보면 됨.
                        # x 혹은 y 의 최댓값과 i, j 의 최댓값을 생각 하자. x의 최댓값은 (n * 2) - 1, i 의 최댓값은 (m - 1),
                        # print(x + i, y + j)
                        # print(x, y, i, j)
                        new_lock[x + i][y + j] += key[i][j]

                # 새로운 자물쇠에 열쇠가 맞는지 검사
                if check(new_lock):
                    return True
                # 자물쇠에서 열쇠 제거
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False


# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
