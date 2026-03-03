# Initialize an empty dictionary of student grades
student_grades = {}


# Function to add a student and grade
def add_student(name, grade):
    student_grades[name] = grade
    print(f" {grade} added for student {name}")


# Function to remove a student
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f" {name} removed from list")
    else:
        print(f"{name} not found")


# Function to display all students and their grades
def display_students():
    print("Grades:")
    for name, grade in student_grades.items():
        print(f"- {name}: {grade}")


# Function to update a student's grade
def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f" {name}'s grade updated to {grade}")
    else:
        print(f" {name} not found ")


# Function to find a students grade
def find_grade(name):
    if name in student_grades:
        print(f" {name} has an {student_grades[name]}")
    else:
        print(f" {name} not found")


# Function to calculate average grade
def average_grade():
    total = 0
    for name, grade in student_grades.items():
        total += grade
    print(f" Average: {total/len(student_grades)}")


# Add some students
add_student("Jimothy", 99)
add_student("Timothy", 70)
add_student("Bimothy", 80)
add_student("Rimothy", 85)

# Display students and their grades
display_students()

# Update a student's grade
update_grade("Rimothy", 65)

# Remove a student
remove_student("Bimothy")

# Display students and their grades again
display_students()

# Find Jimothy's grade
find_grade("Jimothy")

# Average grade
average_grade()
