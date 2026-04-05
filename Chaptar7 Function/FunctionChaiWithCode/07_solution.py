# Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.


# def sum_All(*args):
#     return sum(args)

# print(sum_All(1,2,3))
# print(sum_All(1,2,3,4,5))
# print(sum_All(1,2,3,4,5,6,7))
# print(sum_All(1,2,3,4,5,6,7,8,9,10))


# or


def sum_All(*nums):
    sum = 0
    for i in nums:
        sum+=i
    return sum
     

print(sum_All(1,2,3))