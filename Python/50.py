# Python Writing files (.txt, .json, .csv)

import json
import csv
# .txt file
txt_data = "I like biryani"
employees = ["Swapna", "Sony", "Nani", "Indu"]

file_path = "output.txt"

try:
  with open(file_path, "w") as file: #To create a file here the second parameter in open() is mode , "w" - used to write, "x" - also used write if the file path doesnot exsits, "a"-append the child, "r"- read the file 
    file.write(txt_data)
    for employee in employees:
      file.write(employee)
    print(f"The file '{file_path}' was created")
except FileExistsError:
  print("That file already exists")

# .json file

worker = {
  "name" : "Abhiram",
  "age": 30,
  "job": "SDE"
}

file_path = "output.json"

try:
  with open(file_path, "x") as file:
    json.dump(worker, file, indent=4)
    print(f"The json '{file_path} was created'")
except FileExistsError:
  print("The file is already created")

# .csv file

workers = [["Name", "Age", "Job"],
 ["Spongebob", 30, "cook"], 
 ["Tanjiro", 22, "Fighter"], 
 ["Zenistu", 23, "Fighter"]]

file_path = "output.csv"

try:
  with open(file_path, "x", newline="" ) as file:
    writer = csv.writer(file) #writer is an object, it provides methods for writing data to a csv file
    for row in workers:
      writer.writerow(row)
    print(f"The csv '{file_path}' was created")
except FileExistsError:
  print("The file is already created!")