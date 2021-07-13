def solution(n):
    num = [1, 2, 4]

    answer = ''

    while True:
        n -= 1

        temp = n % 3

        n //= 3

        answer = str(num[temp]) + answer

        if n <= 0:
            break


    return answer




