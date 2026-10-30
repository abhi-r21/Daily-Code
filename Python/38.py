# Inheritance = Allows a class to inherit(means reuse code from one class) attributes and methods from another class
# helps with code reusability and extensibility 
# class Child(Parent)

class Animal:
  def __init__(self, name):
    self.name = name
    self.is_alive = True
  
  def eat(self):
    print(f"{self.name} is eating")
  
  def sleep(self):
    print(f"{self.name} is sleeping")

class Dog(Animal):
  def speak(self):
    print("BOW BOW!")

class Cat(Animal):
  def speak(self):
    print("MEOW MEOW!")
class Duck(Animal):
  def speak(self):
    print("QWAK QWAK")

dog = Dog("Harry potter")
cat = Cat("Mrs.Norris")
duck = Duck("MikeTyson")

