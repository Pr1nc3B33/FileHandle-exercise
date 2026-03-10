
"""Part 1: Class Definition

Create a class called Student with the following attributes:
name (string)
email (string)
grades (list of integers)
Add the following methods:
add_grade(self, grade): Adds a grade to the grades list.
average_grade(self): Returns the average of all grades.
display_info(self): Prints the student’s name, email, and grades."""


class Student:    
    def __init__(self, name, email):
        """Initialize the Student object with name and email."""
        self.name = name
        self.email = email
        self.grades = []  # Initialize an empty list to store grades

    def add_grade(self, grade):
        """Add a grade to the student's list of grades."""
        self.grades.append(grade)

    def average_grade(self):
        """Calculate and return the average of the student's grades."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """Display the student's information."""
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")


"""Part 2: Working with Objects

Create 3 student objects with different names, emails, and initial grades.
Add 2 new grades to each student using the add_grade method.
Print the information and average grade for each student using display_info."""

# Create student objects
student1 = Student("Alice Smith", "alice.smith@example.com")
student2 = Student("Bob Johnson", "bob.johnson@example.com")
student3 = Student("Charlie Brown", "charlie.brown@example.com")

# Add initial grades
student1.add_grade(85)
student1.add_grade(90)
student2.add_grade(78)
student2.add_grade(82)
student3.add_grade(92)
student3.add_grade(88)

# Add 2 new grades to each student
student1.add_grade(95)
student1.add_grade(87)
student2.add_grade(80)
student2.add_grade(85)
student3.add_grade(90)
student3.add_grade(93)

# Print information and average grade for each student
student1.display_info()
print(f"Average Grade: {student1.average_grade()}\n")

student2.display_info()
print(f"Average Grade: {student2.average_grade()}\n")

student3.display_info()
print(f"Average Grade: {student3.average_grade()}\n")   

"""Part 3: Dictionary & Set Integration

Create a dictionary called student_dict that maps each student’s email to their corresponding Student object.
Write a function get_student_by_email(email) that retrieves a student object from the dictionary safely using .get().
Create a set of all unique grades across all students and print it."""

# Create a dictionary to map student emails to Student objects
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Function to retrieve a student by email
def get_student_by_email(email):
    return student_dict.get(email)

# Create a set of all unique grades across all students
unique_grades = set()
for student in student_dict.values():
    unique_grades.update(student.grades)

print(f"Unique Grades: {unique_grades}")    

"""Part 4: Tuple Practice

Add a method to the Student class called grades_tuple(self) that returns the grades as a tuple.
Demonstrate that tuples are immutable by trying to change a value 
(catch the exception with try/except and print a message)."""

class Student:
    def __init__(self, name, email):
        """Initialize the Student object with name and email."""
        self.name = name
        self.email = email
        self.grades = []  # Initialize an empty list to store grades

    def add_grade(self, grade):
        """Add a grade to the student's list of grades."""
        self.grades.append(grade)

    def average_grade(self):
        """Calculate and return the average of the student's grades."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """Display the student's information."""
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")

    def grades_tuple(self):
        """Return the grades as a tuple."""
        return tuple(self.grades)
    
# Create a student object
student1 = Student("Alice Smith", "alice.smith@example.com")

# Add some grades
student1.add_grade(85)
student1.add_grade(90)  

# Get grades as a tuple
grades_as_tuple = student1.grades_tuple()
print(f"Grades as tuple: {grades_as_tuple}")

# Demonstrate that tuples are immutable
try:
    grades_as_tuple[0] = 100
except TypeError as e:
    print(f"Error: {e} (Tuples are immutable)") 
    
    
"""Part 5: List Operations

Remove the last grade from each student’s grades list using .pop().
Access and print the first and last grade for each student.
Print the number of grades each student has using len().    """

# Remove the last grade from each student's grades list
student1.grades.pop()
student2.grades.pop()
student3.grades.pop()

# Access and print the first and last grade for each student
print(f"{student1.name} - First Grade: {student1.grades[0]}, Last Grade: {student1.grades[-1]}")
print(f"{student2.name} - First Grade: {student2.grades[0]}, Last Grade: {student2.grades[-1]}")
print(f"{student3.name} - First Grade: {student3.grades[0]}, Last Grade: {student3.grades[-1]}")

# Print the number of grades each student has
print(f"{student1.name} - Number of Grades: {len(student1.grades)}")
print(f"{student2.name} - Number of Grades: {len(student2.grades)}")
print(f"{student3.name} - Number of Grades: {len(student3.grades)}")    

"""Part 6: Bonus (Optional)

Use regular expressions to validate that each student’s email follows the format: name@domain.com.
Count how many grades are above 90 across all students."""

import re
# Regular expression pattern for validating email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
# Validate each student's email
for student in student_dict.values():
    if re.match(email_pattern, student.email):
        print(f"{student.name}'s email is valid.")
    else:
        print(f"{student.name}'s email is invalid.")    
# Count how many grades are above 90 across all students
count_above_90 = 0
for student in student_dict.values():
    count_above_90 += sum(1 for grade in student.grades if grade > 90)
print(f"Number of grades above 90: {count_above_90}")
