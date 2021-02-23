# 대표값
def representative_value(n, list):
    # 5 <= n 100
    # 학생의 번호는 1 부터 시작.

    avg = sum(list) / n

    student_num = 1
    student_score = list[student_num]
    min_avg = abs(list[student_num] - avg)

    # print(avg)

    for x in range(1, n):
        if abs(list[x] - avg) < min_avg:
            print(x)
            student_num = x + 1
            student_score = list[x]
            min_avg = abs(list[x] - avg)

    print(student_num, student_score)

representative_value(10, [45, 73, 66, 87, 92, 67, 75, 79, 75, 80])
# representative_value(20, [13, 34, 17, 6, 11, 15, 27, 42, 39, 31, 25, 36, 32, 25, 17, 45, 67, 89, 24, 65])

# 개선
def representative_value2(n, list):
    # python 에서 round 는 사사오입의 개념. 4.5 => 4, 5.5 => 6
    avg = int((sum(list) / n) + 0.5)

    min = abs(list[0] - avg)
    student_score = list[0]
    student_num = 1

    for index, score in enumerate(list):
        temp = abs(score - avg)

        if temp < min:
            min = temp
            student_score = score
            student_num = index + 1
        elif temp == min:
            if score > student_score:
                student_score = score
                student_num = index + 1
    print(avg, student_num)

representative_value2(10, [45, 73, 66, 87, 92, 67, 75, 79, 75, 80])
# representative_value2(20, [13, 34, 17, 6, 11, 15, 27, 42, 39, 31, 25, 36, 32, 25, 17, 45, 67, 89, 24, 65])