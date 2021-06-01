# 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수

def solution(s):
    zero_stack = []
    one_stack =[]

    zero_count = 0
    con_count = 0

    pivot = s

    while pivot != "1":
        for x in pivot:
            if x == "0":
                zero_stack.append(x)
                zero_count += 1
            elif x == "1":
                one_stack.append(x)

            print(one_stack)
            print(zero_stack)

            binary = bin(len(one_stack))

            pivot = (str(binary[2:]))

            print("binary", binary)
            print("pivot", pivot)

            if binary == 0b1:
                break
            else:
                zero_stack.clear()
                one_stack.clear()
                con_count += 1


    print(zero_count)
    print(con_count)


    # print(bin(len(stack)))

    # print(bin(6))

    # print(0b11)



print(solution("1111111"))