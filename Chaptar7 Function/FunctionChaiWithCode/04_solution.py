# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

# Area of Circle = A=πr2
# Area of circumference = C = 2 × π × r

def area(r):
    area = 3.14 * r * r
    circumference = 2 * 3.14 * r
    return [area, circumference]

result = area(3)
print(result)
