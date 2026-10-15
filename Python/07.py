#String methods

name = input("Enter you full name: ")
phone_number = input("Enter your Phone Number: ")

result=len(name)
result=name.find(" ")
result=name.rfind(" ") #reverse
result=name.capitalize()
result=name.upper()
result = name.isdigit()
result=name.isalpha()
result=phone_number.count(" ")
result=phone_number.replace("-", " ")

print(result)
