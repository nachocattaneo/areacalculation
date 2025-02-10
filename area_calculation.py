import math


radius = float(input("Please provide with the radius in cm of the circle for which you wish to know the area of: "))

area = math.pi * (radius ** 2)

print(f"The area of the circle that has {radius} cm of radius is {area} cm2")