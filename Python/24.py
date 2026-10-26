#default arguments = A default value for certain parameters, default is used when that argument is omitted , make your functions more flexible, reduces # of arguments 
# 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

import time

def count(end, start=0):
  for x in range(start, end+1):
    print(x)
    time.sleep(1)
  print("DONE!")

count(10)

#keyword arguments = an argument preceded by an indentifier, helps with readability, order of argument doesn't matter.
# 1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def hello(greeting, title, firstName, lastName):
  print(f"{greeting} {title} {firstName} {lastName}")

hello("Hello", "Mr.", "Abhiram", "Bojja")

def get_phone(country, area, first, last):
  return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)