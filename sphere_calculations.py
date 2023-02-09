"""Exercise 8: Calculate area and volume of sphere"""

PI = 3.14159

radius = float(input("Radius: "))

volume = (4/3)*PI*(radius**3)
area = 4*PI*(radius**2)

print(f"Area is {round(area, 2)} square cm")
print(f"Volume is {round(volume, 2)} cubic cm")
