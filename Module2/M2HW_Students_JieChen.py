# A brief description of the project
# 3/20/20
# CSC121 M2HW – Students Class
# Jie Chen

# No Inputs
# Create a class call students
# Create 3 student objects
# Then the program will display student info in a tabular format


class Students:
    """This class holds student's id#, firstName, lastName, and their major"""

    def __init__(self, studentId, firstName, lastName, major):
        self._id = studentId
        self._fn = firstName
        self._ln = lastName
        self._major = major

    def __repr__(self):
        return f"Students(studentId={self._id}, firstName={self._fn}, lastName={self._ln}, major={self._major}"


student1 = Students(47899, "Susan", "Meyers", "Accounting")
student2 = Students(39119, "Mark", "Jones", "Programmer")
student3 = Students(81774, "Joy", "Rogers", "Engineering")

students = [student1, student2, student3]

print("-"*30)
print("ID Number\tFirst Name\tLast Name\tMajor")
for student in students:
    print(f"{student._id:<15}\t{student._fn:>10}\t{student._ln:>9}\t{student._major:>10}")
