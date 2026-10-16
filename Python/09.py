#while loop = execute some code while some condition remains true

enterName = input("Enter your name: ")

while enterName == "":
  print("You haven't entered your name")
  enterName = input("Please enter your name my dear friend: ")

print(f"Hello {enterName}, Nice to meet you..!!!")