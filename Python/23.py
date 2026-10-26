#function = A block of reusable code
# place () after the function name to invoke it 

def happy_birthday(name, age):
  print(f"Happy Birthday to {name}")
  print(f"Your are {age} old years!!")

happy_birthday("Steve", 35)

def display_invoice(username, amount, due_date):
  print(f"Hello {username}, Your bill of ${amount} is due: {due_date}")

display_invoice("BirthDay Boy", 200, "01/11/2026")

#return = statement used to end a function
# and send a result back to the caller 

def create_name(first, last):
  first = first.capitalize()
  last = last.capitalize()
  return first + " " + last

full_name = create_name("abhiram", "bojja")
print(full_name)

def add(x, y):
  z = x + y
  return(z)

def subtract(x, y):
  z = x - y
  return(z)

def multiply(x, y):
  z = x * y
  return(z)

def divide(x, y):
  z = x / y
  return(z)

print(add(3, 5))
print(subtract(10, 6))
print(multiply(586, 985))
print(divide(562, 12))