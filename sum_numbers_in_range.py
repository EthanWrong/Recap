"""Exercise 2: Sum numbers in range"""

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

numbers = []
for i in range(num1, num2+1):
    numbers.append(i)

print(f"Sum is {sum(numbers)}")
