#super() = Function used in a child class to call methods from a parent class (superclass).
# Allows you to extend the functionality of the inherited methods

class Shape:
  def __init__(self, color, is_filled):
    self.color = color
    self.is_filled = is_filled

  def describe(self):
    print(f"The color of the square is {self.color}, it's {'True' if self.is_filled else 'False'} that its color is filled.")
  
class Circle(Shape):
  def __init__(self, color, is_filled, radius):
    super().__init__(color, is_filled)
    self.radius = radius

  def describe(self):
    print(f"Its a Circle with the area of {3.14 * self.radius * self.radius}cm^2")
    super().describe()
  
class Square(Shape):
  def __init__(self, color, is_filled, side):
    super().__init__(color, is_filled)
    self.side = side

class Rectangle(Shape):
  def __init__(self, color, is_filled, length, width):
    super().__init__(color, is_filled)
    self.length = length
    self.width = width

circle = Circle(color="red", is_filled=True, radius=5)

circle.describe()