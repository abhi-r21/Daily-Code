# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#   *unpacking operator
# 1. positional, 2. default, 3. keyword, 4. ARBITRARY

def add(*args):
  total = 0
  for arg in args:
    total += arg
  return total

print(add(1, 2, 3, 10, 50))

def display_name(*args):
  for arg in args:
    print(arg, end=" ")

display_name("Salaar", "Devaratha", "Raisaar", "Shouryanga")

def display_address(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}:{value}")

display_address(
street="123 Fake St.",
apt="100",
city="New York",
state="US state",
pincode="54321")

def shipping_label(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")
  print()
  
  if "apt" in kwargs:
   print(f"{kwargs.get('street')} {kwargs.get('apt')}")
  elif "pobox" in kwargs:
    print(f"{kwargs.get('pobox')}")
    print(f"{kwargs.get('street')}")
  else:
    print(f"{kwargs.get('street')}")

  print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('pincode')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
street="123 Fake St.",
apt="100",
city="New York",
state="US",
pincode="54321")