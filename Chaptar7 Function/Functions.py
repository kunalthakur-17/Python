num1 = 10
num2 = 20

def sum (a,b):
    result = a + b
    return result

print(sum(num1,num2))
# print(sum(2,10))
# print(sum(22,10))
# print(sum(44,10))
# print(sum(33,10))
# print(sum(11,10))


def hello():
    return "hello"

result = hello()

print(result)


# average of 3 number

def agerageOfthreeNum(a,b,c):
    sum = a+b+c
    avg = sum/3
    return avg

agerageOfthreeNumResutl = int(agerageOfthreeNum(1,2,3))
print(agerageOfthreeNumResutl)