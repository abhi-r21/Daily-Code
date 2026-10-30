# object = A "bundle" of related attributes (varibles) and methods (functions)
# Ex. phone, cup, book
# you need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object

class Car:
  def __init__(self, model, year, color, for_sale): #This is known as constructor in a class , and it helps to set up an object when we create it 
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale
    #these model, year, color, for_sale are known are attributes or varibles
  
  def drive(self):
    print(f"You drive the {self.model}")
  def stop(self): 
    print(f"You stop the {self.model}")
    # these functions drive() and stop() are known are methods , methods are functions that belong to an object & they decide what this object can do 

car1 = Car("Mustang", 2024, "black", False) #attributes
car2 = Car("BMW 320d", 2013, "Orange and black", True) #attributes

car1.drive()
  
 