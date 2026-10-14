#Python weight convertor

weight = int(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L) : ")

if unit == "K":
  weight = weight * 2.205
  unit = "Lbs"
  print(f"Your weight is : {round(weight)} {unit}")
elif unit == "L":
  weight = weight / 2.205
  unit = "Kgs"
  print(f"Your weight is : {round(weight)} {unit}")
else :
  print(f"{unit} is a invaild unit")