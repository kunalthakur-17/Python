# Create a dictionary named marks to store marks of 3 subjects.
# Add the subjects one by one and print the final dictionary.


subject = {}

subject["English"] = 88
subject["Physics"] = 87
subject["Chemistry"] = 92
subject['Maths'] = 90

print(subject)

# student = {"name":"Kunal", "age":20}
# print(student.get("gender", "Not Found"))
# Create a dictionary of 3 students with their marks and print the one with highest marks.

student = {
    'English': 88, 'Physics': 87, 'Chemistry': 92, 'Maths': 90
}

print(student['Chemistry'])