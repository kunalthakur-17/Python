# count postive number
# number = [-1,2,-3,-4,5,8,9,-3,-6]
# ele = 0
# while ele < len(number):
#     if number[ele] > 0:
#         print(number[ele])
#     ele += 1
   
# or

# for num in number :
#     if(num>0):
#         ele+=1
        
# print(ele)


# sum of even number upto given no X from list


# evenNumberLinst = [1,2,3,4,5,6,7,76,88,65,89,44,33,22]
# sumofeventnumber = 0
# x = 40

# for num in evenNumberLinst :
#     if(num % 2 == 0 and num >= x):
#         sumofeventnumber += num
# print(sumofeventnumber)

# sum of even number upto given no X

# sumOfEvenNum = 10
# sum = 0

# for i in range(1,sumOfEvenNum+1):
#     if(i%2==0):
#         sum+=i
# print(sum)


# x table up to 10 ans skip 5 iteration
ele = 1
x = 5


# while ele <= 10 :
#     if(ele == 5):
#         ele+=1
#         continue
#     print(f"{x} X {ele} = {x*ele}")
#     ele+=1

    # or 
for i in range(1,11):
    if(i==5):
        continue
    print(f"{x} X {i} = {x*i}")
    i+=1