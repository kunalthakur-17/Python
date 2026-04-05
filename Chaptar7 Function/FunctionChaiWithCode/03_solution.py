# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a, b):
    return a * b

# Test cases
print(multiply(10, 20))      # 200
print(multiply("Hi", 3))     # HiHiHi
print(multiply(3, "Hello")) 
