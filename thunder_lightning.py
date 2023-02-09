"""Exercise: Calculates distance of lightning"""

seconds = float(input("How many seconds apart was the "
                      "lightning and thunder? "))

distance = seconds * 340
distance_km = round(distance / 1000, 3)

print(f"The storm is about {distance_km}km away")