# Math Examples
import math
'''
friends = 6

# friends = friends + 1
friends += 1
print(friends)

# friends = friends - 2
friends -= 2
print(friends)

# friends = friends * 3
friends *= 4
print(friends)

# friends = friends / 2
friends /= 2
print(friends)

friends **= 2
print(friends)

remainder = friends % 3
print(remainder)

x = 3.14
y = -4
z = 5

result = round(x)
print(f"{x} rounded is {result}")

result = abs(y)
print(f"The absolute value of {y} is {result}")

result = pow(z, z)
print(f"{z} to the power of {z} is {result}")

result = max(x, y, z)
print(f"The max value of {x}, {y}, and {z} is {result}")

print(math.pi)
print(math.e)
# math.sqrt(z) Square Root
# math.ceil(x) Rounds Up
# math.floor(x) Rounds Down
'''

# Circumference Problem

radius = float(input("Enter the radius of a circle: "))
circumference = radius * math.pi * 2.0
print(f"The circumference of the circle is {round(circumference, 3)}")

# Area Problem

area = pow(radius, 2) * math.pi
print(f"The area of the circle is {round(area, 3)}")

# Hypotenuse Problem
length = float(input("Enter the length of a triangle: "))
height = float(input("Enter the height of a triangle: "))
hypotenuse = math.sqrt(pow(length, 2) + pow(height, 2))
print(f"The hypotenuse of the triangle is {round(hypotenuse, 2)}")
