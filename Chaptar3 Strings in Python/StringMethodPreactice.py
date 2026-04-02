# Write a program that take a sentence as input 
# and convert it in lower case
# Replace all space in _
sentence = input("Enter a sentence: ")
lowerCase = sentence.lower()
result = lowerCase.replace(" ", "_")
print(result)