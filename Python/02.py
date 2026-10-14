#Simple calculater

operater = input("Enter your operater(+ - * /): ")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

if operater == "+":
  result = num1 + num2
  print(result)
elif operater == "-":
  result = num1 - num2
  print(result)
elif operater == "*":
  result = num1 * num2
  print(result)
elif operater == "/":
  result = num1 / num2
  print(result)

