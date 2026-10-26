# Membership operators = used to test whether a value or variable is found in a sequence
# (string, list, tuple, set, or dictionary)
# 1. in
# 2. not in

#string

word = "APPLE"

letter = input("Guess the letter in the word: ").upper()

# in 
if letter in word:
  print(f"There is a {letter}")
else:
  print(f"{letter} is not there.")

# not in
if letter not in word:
  print(f"{letter} was not found")
else:
  print(f"There is a {letter}")

#List , tuple , set - these behave similarly
students = {"Tylor", "Durdin", "Peter"}
student = input("Enter the name of student: ")

# in
if student in students:
  print(f"Yes, {student} is there")
else:
  print(f"No, {student} there is not student with the name {student}")

#for "not in" reverse the conditions 

#dictonary

grades = {
  "Sandy": "A",
  "Candy": "B",
  "Randy": "C",
  "Nandy": "D"}

student = input("Enter the name of a student: ")

if student in grades:
  print(f"{student}'s grade is {grades[student]}")
else:
  print(f"There is no such student with name {student}")

#another example

email = "tonystark@gmail.com"

if "@" in email and "." in email:
  print("Email is Valid")
else:
  print("Email is InValid, Please check your email")