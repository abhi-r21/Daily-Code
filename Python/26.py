#Iterables = An object/colletction that can return its elements one at a time 
# allowing it to be iterated over in a loop

#List
numbers = [1, 2, 3, 4, 5]

for number in numbers:
  print(number, end=" ")

print()

for number in reversed(numbers):
  print(number, end=" ")

print()

#Tuple
numbers = (1, 2, 3, 4, 5)

for number in numbers:
  print(number, end=" ")

print()

#Set
fruits = {"apple", "banana", "orange", "pineapple"}

for fruit in fruits:
  print(fruit, end=" ")

print()

#String
name = "Micheal Jackson"

for character in name:
  print(character, end="")

print()

#dictionary
user={
  "name": "Micheal",
  "age": 22
}

for key, value in user.items():
  print(f"{key} : {value}")