# if __name__ == __main__ : (this script can be imported OR run standalone)
# Functions and classes in this module can be reused
# without the main block of code executing

# helper.py
def greet():
    print("Hello!")

if __name__ == "__main__":
    print("Running directly")

#We get the result "Running directly" if we run python helper.py

# app.py
import helper
helper.greet()

#we will get the result "Hello!" if we run python app.py