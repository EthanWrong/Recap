"""Code that keeps track of concrete volumes"""
def calculate_volume(length, width, type):

    depth = 0.5 if type.lower() == "c" else 0.25
    # if type.lower() == "c":
    #     depth = 0.5
    # else:
    #     depth = 0.25

    volume = length*width*depth
    print(f"The volume of concrete required for a slab with a length of {length} and a width of {width} and a depth of"
          f" {depth} is {volume} cubic metres.")
    return volume


running_total = 0.0

print("Concrete Volume Calculator")

while True:
    building_type = input("R or C: ").lower()
    while building_type not in ("r", "c", "x"):
        building_type = input("Residential (r) or Commercial (c), or Exit (x): ").lower()
    
    if building_type == "x":
        print(f"Total concrete is {running_total} cubic metres.")
        break

    length = float(input("Length: "))
    width = float(input("Width: "))
    running_total += calculate_volume(length, width, building_type)

