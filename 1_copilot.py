#list of three students named Jon, Kim and Lee 
students = ["Jon", "Kim", "Lee"]
# Add Sara and Miko to the list
students.append("Sara")
students.append("Miko")

# Function to print ‘Hi name’ for each student and total number of students
def greet_students(students):
    for student in students:
        print(f"Hi {student}")
    print(f"Total number of students: {len(students)}")

# Call the function
greet_students(students)
# change Jon to John
students[1] = 'John'
