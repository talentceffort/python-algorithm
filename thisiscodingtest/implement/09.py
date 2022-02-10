def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        # print('prev1', prev)
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            # 더 이상 압축 불가
            else:
                # 파이썬의 3항 연산자.
                compressed += str(count) + prev if count >= 2 else prev
                # prev 초기화
                prev = s[j:j + step]
                count = 1

        # print('count', count)
        # print('prev', prev)
        compressed += str(count) + prev if count >= 2 else prev
        # print('compressed', compressed)
        answer = min(answer, len(compressed))


    # print('prev', prev)
    # print('count', count)
    # print('compressed', compressed)
    # 남아 있는 문자열 처리



    return answer


print(solution("aabbaccc"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("abcabcdede"))
