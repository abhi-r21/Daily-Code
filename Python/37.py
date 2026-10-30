# class variables = Shared among all the instances(means object created from a class) of class
# defined outside the constructor , Allow you to share data among all objects created from that class

class Student:

  class_year = 2024
  num_students = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Student.num_students += 1

student1 = Student("Hermoine Granger", 17)
student2 = Student("Ronald Weasley", 17)
student3 = Student("Harry Potter", 17)
studnet4 = Student("Lucious Malfoy", 17)

print(f"Hello, My name is {student1.name}. My graduating class of {Student.class_year} has {Student.num_students} students & my best friends are {student2.name} and {student3.name}. And the person I loved during my school time is {studnet4.name}")