"""Exercise 6: Program that calculates number of kilograms worked of during
exercising"""


def calculate_weight_lost(activity, hours):
    if activity == "b":
        calories_lost = 200*hours
    elif activity == "j":
        calories_lost = 475*hours
    elif activity == "s":
        calories_lost = 275*hours
    return (calories_lost/3500) * 454


print("Enter each activity, followed by the number of hours spent on each one."
      " \nEnter 'x' to get your result.")
print()

total_weight_loss = 0

while True:
    activity = input("Were you...\n Bicycling (b)\n Jogging (j) \n Swimming "
                     "(s)\n >>> ")
    if activity not in ("b", "j", "s", "x"):
        continue
    if activity == "x":
        break

    hours = float(input("For how long? >>> "))

    total_weight_loss += calculate_weight_lost(activity, hours)
    print()
    print(f"You lost {round(calculate_weight_lost(activity, hours))}g doing "
          f"that")
    print()

print(f"You lost a total of {round(total_weight_loss)}g")


