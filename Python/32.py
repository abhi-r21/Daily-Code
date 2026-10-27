#Python Banking Program

def show_balance(balance):
  print("--------------------")
  print(f"Your balance is ${balance:.2f}")
  print("--------------------")

def deposit():
  print("--------------------")
  amount = float(input("Enter the amount you would like to deposit: "))
  print("--------------------")

  if amount < 0:
    print("--------------------")
    print("That's not a valid amount")
    print("--------------------")
    return 0
  else:
    return amount

def withdraw(balance):
  print("--------------------")
  amount = float(input("Enter the amount to be withdrawn: "))
  print("--------------------")

  if amount > balance:
    print("--------------------")
    print("Insufficiant balance")
    print("--------------------")
    return 0
  elif amount < 0:
    print("--------------------")
    print("Amount should be greater than 0")
    print("--------------------")
    return 0
  else: 
    return amount


def main():
  balance = 0 
  is_runnning = True

  while is_runnning:
    print("--------------------")
    print("Banking Program")
    print("--------------------")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("--------------------")

    choice = input("Please select your option(1-4): ")

    if choice == "1":
      show_balance(balance)
    elif choice == "2":
      balance += deposit()
    elif choice == "3":
      balance -= withdraw(balance)
    elif choice == "4":
      is_runnning = False
    else:
      print("--------------------")
      print("Invalid Input")
      print("--------------------")

  print("--------------------")
  print("Thank you! Have a nice day!")
  print("--------------------")

if __name__ == '__main__':
  main()