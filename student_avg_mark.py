"""Program that keeps track of student marks and grades"""


def add_student(name, mark, students):
    if name not in students:
        students[name] = []
    students[name].append(mark)


def find_average_mark(students):
    total = 0
    count = 0
    for i in students:
        for j in students[i]:
            total += j
            count += 1
    average_mark = total/count
    print(f"The average mark was {average_mark}")


def find_top_mark(students):
    top_mark = 0
    top_student = ""
    for i in students:
        for j in students[i]:
            if j > top_mark:
                top_mark = j
                top_student = i
    print(f"Top student was {top_student} with a mark of {top_mark}")


# main routine

my_students = {}

while True:
    name = input("Name: ").lower()
    if name == "x":
        break
    mark = int(input("Mark: "))

    add_student(name, mark, my_students)

find_average_mark(my_students)
find_top_mark(my_students)