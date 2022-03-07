from sys import stdin

stdin = open("10825.txt")

n = int(stdin.readline())

students = []

for i in range(n):
    data = stdin.readline().split()
    students.append(data)


sorted_students = sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for x in sorted_students:
    print(x[0])