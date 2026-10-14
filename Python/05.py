#Logical Operators

temp = 50 #input any temperature value
is_sunny = True

if temp >= 20 and is_sunny:
  print("It is sunny outside")
elif temp <= 20 or is_sunny:
  print("It's warm outside")
elif temp >= 30 and not is_sunny:
  print("It's Hot outside")