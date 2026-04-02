
foods = ["Samosa", "Pizza", "Burger", "Furits","Cake"]
print("old list",foods)
# Modifying Elements
foods[0]= "Hen"
print("new list",foods) #new list ['Hen', 'Pizza', 'Burger', 'Furits', 'Cake']
# foods[1]= "" 
# print(foods)  #['Hen', '', 'Burger', 'Furits', 'Cake']

# List Functions

list =  [87, 64, 33, 95, 76]
totalLength = len(list)
print("This is Total Length of list", totalLength) #5
# largest Number
largestNumber = max(list)
print(largestNumber) # 95
# smallest number
smallestNumber = min(list) #33
print(smallestNumber)

# Common List Methods

marks =[10,20,40,55,55,44,57,86,67]

marks.append(99)
print(marks) # [10, 20, 40, 55, 55, 44, 57, 86, 67, 99]

marks.insert(1,0)
print(marks) #[10, 0, 20, 40, 55, 55, 44, 57, 86, 67, 99]
marks.remove(40)
print(marks) #[10, 0, 20, 55, 55, 44, 57, 86, 67, 99]
marks.pop(0)
print("remove using index no",marks) #[0, 20, 55, 55, 44, 57, 86, 67, 99]
marks.reverse()
print(marks) #[99, 67, 86, 57, 44, 55, 55, 20, 0]