from sys import stdin

stdin = open("02.txt")

input = stdin.readline

s = list(map(int, input()))

result = s[0]

# 두 수 중에서 하나라도 0, 1이면 더하는게 이득
# 두 수가 모두 2 이상일 때 곱하자

for i in range(1, len(s)):
    val = s[i]
    if val == 0 or result == 0:
        result += val
    elif val == 1:
        result += val
    else:
        result *= val

    # if val <= 1 or result <= 1:
    #     result += val
    # else:
    #     result *= val



print(result)