"""Exercise 1: finds biggest number of two inputs"""


while True:
    num1 = int(input("Enter first number: "))
    if num1 == 0:
        break
    num2 = int(input("Enter second number: "))
    if num2 == 0:
        break
    
    if num1 == num2:
        print("They are even")
    elif num1 > num2:
        print(f"{num1} is bigger")
    else:
        print(f"{num2} is bigger")