# Static methods = A method that belongs to a class rather than any object from that class(instance)
#  Usually used for general utility functions
# Instance methods = Best for operations on instances of the class(Objects)
# Static methods =  Best for utility functions that do not need access to class data

from logging import Manager


class Employee:

  def __init__(self, name, position):
    self.name = name
    self.position = position

  def get_info(self): #This is known as Instance Method
    return f"{self.name} = {self.position}"

  @staticmethod #for static method you only need to access the class , we dont need to create objects 
  def is_valid_position(position):
    valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]

    return position in valid_positions

# These are the instance of the class
employee1 = Employee("George",  "Manager")
employee2 = Employee("Sheldon", "Cashier")
employee3 = Employee("Lenord", "Cook")
employee4 = Employee("Rajesh Kuthrapoli", "Janitor")

print(Employee.is_valid_position("Manager"))

#To call the instance method we need access intances of the class
# For instance method, we access an object and then call the instance method
print(employee1.get_info())