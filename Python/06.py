#Conditional Expression = A one-line shortcut for the if/else coditions (also know as Ternary operator). Print or assign one of two values based on the condition . X if condition else Y 

num = 5
a = 10
b = 15
age = 20
temp = 30 
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "Odd"
print(result)

max_num = a if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

status = "Your are eligible for applying license" if age > 18 else "Your are not eligible for applying license"
print(status)

print("Weather is Hot" if temp > 20 else "Weather is cold")

print("You can get full access" if user_role == "admin" else "You will get limited access only") 