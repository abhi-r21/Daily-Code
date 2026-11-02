# Python reading files (.txt, .json, .csv)

# to read .csv file
import csv

file_path = "something.csv"

try:
  with open(file_path, "r") as file:
    content = csv.reader(file)
    for line in content:
     print(line)
except FileNotFoundError:
  print("This file is not found!")
except PermissionError:
  print("You don't have permission to read that file")

# to read .json file
import json

file_path = "something.json"

try:
  with open(file_path, "r") as file:
    content = json.load(file)
    print(content)
except FileNotFoundError:
  print("This file is not found!")
except PermissionError:
  print("You don't have permission to read that file")

# to read .txt file
file_path = "something.txt"

try:
  with open(file_path, "r") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
  print("This file is not found!")
except PermissionError:
  print("You don't have permission to read that file")