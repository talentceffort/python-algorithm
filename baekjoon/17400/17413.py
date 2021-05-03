import sys

sys.stdin = open("17413.txt")

T = sys.stdin.readline()

in_tag = False

words = []

reverse = []


for x in T:
    if x == '<':
        while reverse:
            words.append(reverse.pop())
        in_tag = True
        words.append(x)
    elif x == '>':
        in_tag = False
        words.append(x)
    elif in_tag:
        words.append(x)
    elif in_tag == False and x == ' ':
        while reverse:
            words.append(reverse.pop())
        words.append(x)
    elif in_tag == False:
        reverse.append(x)


if reverse:
    while reverse:
        words.append(reverse.pop())

print(''.join(words))


# text = list(input())
#
# flag = False
#
# result = []
# temp = []
# for i, t in enumerate(text):
#     if t == "<":
#         if len(temp) > 0:
#             temp.reverse()
#             result.extend(temp)
#             temp = []
#         flag = True
#         temp.append(t)
#     elif t == ">":
#         flag = False
#         temp.append(t)
#         result.extend(temp)
#         temp = []
#     elif t == " ":
#         if flag == False:
#             temp.reverse()
#             temp.append(t)
#             result.extend(temp)
#             temp = []
#         else:
#             temp.append(t)
#     else:
#         temp.append(t)
#         if len(text) == i+1:
#             temp.reverse()
#             result.extend(temp)
#
# print(''.join(result))