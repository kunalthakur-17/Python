# WAF to print the length of a list. ( list is the parameter)

# list = ["Spider-Man", "Black Panther", "Doctor Strange", "Captain Marvel", "Ant-Man", "Black Widow"]

# def caluListLength(list):
#     result = len(list)
#     return result

# print(caluListLength(list))

# WAF to print the elements of a list in a single line. ( list is the parameter)

# def listInSingleLine(list):
#     for item in list :
#         print(item, end=" ")

# listInSingleLine(list)

# WAF to find the factorial of n. (n is the parameter)

# def factorial(n):
#     multply = 1
#     for items in range(1,n+1):
#         multply=multply*items
#     print(multply)

# factorial(5)
# factorial(10)

# WAF to convert USD to INR.

# usd = 10
# def converter(usd):
#     ind = 92.72
#     return usd*ind

# print(converter(10))

# take input in int if number is odd then return odd and if number is even then retun even and if zero then return 

num = int(input("Enter you number : "))

def checkNum(num):
    if num < 0:
        return "Negtive"
    if(num%2==0):
        return "Even"
    elif(num%3==1):
        return "Odd"
    elif(num==0):
        return "Zero"
print(checkNum(num))
