students = []

# Starting a student class
class Student:

    # Set static school name value
    school_name = "Naval Public School"

    # Constructor for Student class
    def __init__(self, name, student_id=123):
        self.name = name  # Constructor setup technique
        self.student_id = student_id  # Constructor setup technique
        students.append(self)

    # Equivalent of Java toString method
    def __str__(self):
        return "Student : " + self.name

    # Method to capitalize the first alphabet of name
    def get_name_capitalize(self):
        return self.name.capitalize()

    # Get School name value
    def get_school_name(self):
        return self.school_name


# HighSchoolStudent is inheriting Student class
class HighSchoolStudent(Student):

    school_name = "DAV School"

    def get_school_name(self):
        return "This is DAV."

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + " - DAV"


# creating object of Student class
mark = Student("mark")

print(mark)

print("After Capitalization - " + mark.get_name_capitalize())

print(Student.school_name)

print(HighSchoolStudent.school_name)

