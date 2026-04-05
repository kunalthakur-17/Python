# list = [1,2,3,4,5,67]

# for el in list:
#     if(el == 5):
#         print(el)


# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# for el in list:
#     print(el)   


# findXfromList = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# x = 9
# idx = 0
# for value in list:
#     if(value==x):
#         print("Number found at idx", idx, value)
#     idx+=1

# WAP to find the factorial of first n numbers. (using for)

# x = 5
# factorial = 1

# for i in range(1, x+1):
#     factorial *= i

# print(factorial)


# Print even numbers from 2 to 20 using for and range.


idx = 2  
while idx <= 20:
    if idx % 2 == 0: 
        print(idx)
    idx += 1  
