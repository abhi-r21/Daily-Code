# variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

name = "Thomas" #Global Variable - its defined outside of the function
def greet():
  message = "Hello" #Local variable - its defined inside of the function
  print(name)
  print(message)

greet()

#Local scope - inside the current function
def calculate():
  result = 200
  print(result)

calculate()

#Enclosed scope = inside an outer function
def outer():
  text = "Hello Tommy"
  def inner():
    print(text)
  inner()

outer()

#Global scope = Defined at module level
app_name = "Roam"
def show_app():
  print(app_name)

show_app()

#Built in scope = Python's built in names like print() and len()
 