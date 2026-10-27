# List comprehension = A concise way to create lists in python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition] 

#traditional way:
doubles=[]
for x in range(1, 11):
  doubles.append(x * 2)
print(doubles)

#List Comprehension:
triples=[x * 3 for x in range(1, 11)]
print(triples)

#Strings
fruits = ["apple", "pineapple", "orange", "muskmelon"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

#including if conditions
numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)
negative_nums = [num for num in numbers if num <= 0]
print(negative_nums)
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)
odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums)

#Another example
grades = [86, 90, 75, 57, 61, 80, 49]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)