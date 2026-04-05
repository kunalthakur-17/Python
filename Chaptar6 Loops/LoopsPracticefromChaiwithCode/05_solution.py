# return non repeter char from string

input_str = "teeter"

for char in input_str:
    if(input_str.count(char)==1):
        print("Non Repeter char is :",char)
        break