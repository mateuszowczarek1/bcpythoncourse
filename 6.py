# friends = 23
# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# friends = 10
# remainder = friends % 3
# print(friends, remainder)

# x = 3.14
# y = 4
# z = 5

# result = round(x)
#result = abs(y)
#result = pow(y, 3)
#result = max(x,y,z)
# result = min(x,y,z)
# print(result)

# -------------------

# import math

# x = 9.1
# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)
# print(result)

# -------------------
# Ex. 1 Circumference of a circle

# import math
#
# radius = float(input("Enter the radius of a circle: "))
#
# circumference = 2 * math.pi * radius
#
# print(f"The circumference is: {round(circumference, 2)}")

# -------------------
# Ex. 1 Area of a circle

# import math
#
# radius = float(input("Enter the radius of a circle: "))
#
# area = math.pi * pow(radius, 2)
#
# print(f"The area of the circle is: {round(area, 2)} cm^2")

# -------------------
# Ex. 2 Hypotenuse of a right triangle

import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The hypotenuse of given right triangle is {c}")


