# exception = An event that interrupts the flow of the program
# (ZeroDivisionError, TypeError, ValueError)
# 1.try, 2.except, 3.finally

try:
  number = int(input("Enter a number: "))
  print(1 / number)
except ZeroDivisionError:
  print("Zero can be divided!")
except TypeError:
  print("Please enter only integers!")
except Exception:
  print("Something went wrong!")
finally:
  print("Do some cleanup")