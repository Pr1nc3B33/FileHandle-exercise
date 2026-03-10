"""Part 1: Class Definition

Create a class called Student with the following attributes:
name (string)
email (string)
grades (list of integers)
Add the following methods:
add_grade(self, grade): Adds a grade to the grades list.
average_grade(self): Returns the average of all grades.
display_info(self): Prints the student's name, email, and grades.
grades_tuple(self): Returns the grades as a tuple.
"""

import re


class Student:
    def __init__(self, name, email):
        """Initialize the Student object with name and email."""
        self.name = name
        self.email = email
        self.grades = []

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


"""Part 2: Working with Objects

Create 3 student objects with different names, emails, and initial grades.
Add 2 new grades to each student using the add_grade method.
Print the information and average grade for each student using display_info.
"""

student1 = Student("Alice Smith", "alice.smith@example.com")
student2 = Student("Bob Johnson", "bob.johnson@example.com")
student3 = Student("Charlie Brown", "charlie.brown@example.com")
students = [student1, student2, student3]

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
for student in students:
    student.display_info()
    print(f"Average Grade: {student.average_grade()}\n")


"""Part 3: Dictionary & Set Integration

Create a dictionary called student_dict that maps each student's email to their corresponding Student object.
Write a function get_student_by_email(email) that retrieves a student object from the dictionary safely using .get().
Create a set of all unique grades across all students and print it.
"""

student_dict = {student.email: student for student in students}


def get_student_by_email(email):
    """Retrieve a student by email safely."""
    return student_dict.get(email)


unique_grades = {grade for student in student_dict.values() for grade in student.grades}
print(f"Unique Grades: {unique_grades}")


"""Part 4: Tuple Practice

Use grades_tuple(self) to return the grades as a tuple.
Demonstrate that tuples are immutable by trying to change a value
(catch the exception with try/except and print a message).
"""

grades_as_tuple = student1.grades_tuple()
print(f"Grades as tuple: {grades_as_tuple}")

try:
    grades_as_tuple[0] = 100
except TypeError as error:
    print(f"Error: {error} (Tuples are immutable)")


"""Part 5: List Operations

Remove the last grade from each student's grades list using .pop().
Access and print the first and last grade for each student.
Print the number of grades each student has using len().
"""

for student in students:
    if student.grades:
        student.grades.pop()

for student in students:
    if student.grades:
        print(
            f"{student.name} - First Grade: {student.grades[0]}, "
            f"Last Grade: {student.grades[-1]}"
        )
    else:
        print(f"{student.name} - No grades available")

for student in students:
    print(f"{student.name} - Number of Grades: {len(student.grades)}")


"""Part 6: Bonus (Optional)

Use regular expressions to validate that each student's email follows the format: name@domain.com.
Count how many grades are above 90 across all students.
"""

email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
for student in student_dict.values():
    if re.match(email_pattern, student.email):
        print(f"{student.name}'s email is valid.")
    else:
        print(f"{student.name}'s email is invalid.")

count_above_90 = sum(
    1 for student in student_dict.values() for grade in student.grades if grade > 90
)
print(f"Number of grades above 90: {count_above_90}")