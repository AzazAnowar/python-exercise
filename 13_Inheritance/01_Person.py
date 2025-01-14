"""
Create a base class Person with attributes name and age. Inherit Student
and Teacher classes with additional attributes such as grade for students and subject
for teachers.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

# Example usage:
student = Student("Real", 28, "A")
teacher = Teacher("Mr. Rifat", 20, "Artificial Intelligence")
print(student.name, student.grade)
print(teacher.name, teacher.subject)