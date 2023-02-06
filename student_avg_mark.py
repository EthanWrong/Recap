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
    return total/count


def find_top_mark(students):
    top_mark = 0
    top_student = ""
    for i in students:
        for j in students[i]:
            if j > top_mark:
                top_mark = j
                top_student = i
    print(f"Top student was {top_student} with a mark of {top_mark}")

my_students = {
    # "m": [1, 2, 3, 4],
    # "h": [10, 20, 30, 40]
}

while True:
    name = input("Name: ").lower()
    if name == "x":
        break
    mark = int(input("Mark: "))

    add_student(name, mark, my_students)

    print(my_students)

my_average_mark = find_average_mark(my_students)
print(my_average_mark)