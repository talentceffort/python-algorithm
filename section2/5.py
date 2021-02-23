# 정다면체
# 두 개 정 N 면체와 M 면체의 두 개의 주사위 던져서 나올 수 있 눈의 합 중 가장 확률이 높은 숫자를 출력
# 정답이 여러개일 경우 오름차순
# N 과 M  4, 6, 8, 12, 20

def Platonic_solid(n, m):
    list = [4, 6, 8, 12, 20]
    if n not in list or m not in list:
        return 'is not Platonic_solid'

    if n == m:
        return n + 1
    elif m > n:
        result = ''
        for num in range(n + 1, m + 2):
            result = str(num) if result == '' else result + ' ' + str(num)
        return result
    else:
        for num in range(m + 1, n + 1):
            result = str(num) if result == '' else result + ' ' + str(num)
        return result


print(Platonic_solid(4, 6))
print(Platonic_solid(4, 8))
print(Platonic_solid(8, 12))
    # 4 * 6 => 5 6 7
    # 4 * 8 => 5 6 7 8 9
    # 8 * 12 => 9 10 11 12 13

#   1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8

# 4 * 4 => 5
# 6 * 6 => 7
# 8 * 8 => 9

#   1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 2 3 4 5 6 7 8
# 3 4 5 6 7 8 9
# 4 5 6 7 8 9 10

#   1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9
# 2 3 4 5 6 7 8 9 10
# 3 4 5 6 7 8 9 10 11
# 4 5 6 7 8 9 10 11 12

#   1 2 3 4 5 6 7 8 9 10 11 12
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 2 3 4 5 6 7 8 9 10 11 12 13 14
# 3 4 5 6 7 8 9 10 11 12 13 14 15
# 4 5 6 7 8 9 10 11 12 13 14 15 16
# 5 6 7 8 9 10 11 12 13 14 15 16 17
# 6 7 8 9 10 11 12 13 14 15 16 17 18
# 7 8 9 10 11 12 13 14 15 16 17 18 19
# 8 9 10 11 12 13 14 15 16 17 18 19 20

