# Write a function greet(name) that prints "Hello <name>". Call it with "Kunal"

name = "Kunal"
def greet(name):
   return "Hello " + name

print(greet(name))

# Write a function square(n) that returns the square of a number. Print square(5)

n = 5

def square(n):
   result= n*n
   return result
print(square(n))

# Write a function sum_list(lst) that returns the sum of all numbers in a list [1,2,3,4,5]. 

list = [1,2,3,4,5]
def sumOfAllElement(my_list):
    total = 0
    for ele in my_list:
        total += ele  
    return total

print(sumOfAllElement(list))


# Write a function factorial(n) that returns the factorial of n. Call it for n=5


def factorial(n):
    multy = 1
    for ele in range(1,n+1):
        multy*=ele
    return multy

print(factorial(5))


# Write a function even_numbers(n) that prints all even numbers from 1 to n. Call it for n=10


def even_numbers(n):
    for ele in range(1,n+1):
        if(ele%2==0):
            print(ele)
        
        

even_numbers(10)
