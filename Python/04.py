#Temperature Conversion Program

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = int(input("Enter the Temperature: "))

if unit == "C":
 temp = round((9 + temp) / 5 + 32)
 print(f"The temperature in Fahrenheit is : {temp} °F")
elif unit == "F":
  temp = round((temp - 32) * 5/9)
  print(f"The temperature in Calsius is : {temp} °C")
else :
  print(f"{unit} is invalid")


