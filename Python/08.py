#validate user input exercise 
#username should not contain more than 12 characters
#username should not contain spaces
#username should not contain digits

username = input("Please choose your Username: ")

if len(username) >= 12 :
  print("Username should be less than 12 characters")
elif not username.find(" ") == -1 :
  print("Invalid username , should not contain spaces")
elif not username.isalpha() :
  print("Invalid username, should contain only alphabets")
else:
  print(f"Hello {username}, Welcome to Fight Club")
