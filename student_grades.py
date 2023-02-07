"""Exercise 5: Advanced program that keeps track of student marks and grades"""


def add_student(name, mark, students):
    if name not in students:
        students[name] = {}
        students[name]["marks"] = []
        students[name]["grades"] = []
    students[name]["marks"].append(mark)
    students[name]["grades"].append(determine_uni_grade(mark))


def find_average_mark(students):
    total = 0
    count = 0
    for i in students:
        for j in students[i]["marks"]:
            total += j
            count += 1
    average_mark = round(total / count)
    average_grade = determine_uni_grade(average_mark)
    print(f"The average mark was {average_mark} and the average grade was {average_grade}")


def find_top_mark(students):
    top_mark = 0
    top_student = ""
    for i in students:
        for j in students[i]["marks"]:
            if j > top_mark:
                top_mark = j
                top_student = i
                top_grade = determine_uni_grade(top_mark)
    print(f"Top student was {top_student.capitalize()} with a mark of {top_mark} and a grade of {top_grade}")


def determine_uni_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 85:
        return "A"
    elif mark >= 80:
        return "A-"
    elif mark >= 75:
        return "B+"
    elif mark >= 70:
        return "B"
    elif mark >= 65:
        return "B-"
    elif mark >= 60:
        return "C+"
    elif mark >= 55:
        return "C"
    elif mark >= 50:
        return "C-"
    elif mark >= 40:
        return "D"
    else:
        return "E"


def print_students(students):
    for i in students:
        row = i.capitalize().ljust(10, " ")
        for j in students[i]["grades"]:
            row += j.ljust(3, " ")
        print(row)


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

# print entire list
print_students(my_students)
