#shopping cart program

foods=[]
prices=[]
total=0

while True:
  food = input("Please enter the food you want(q to Quit): ")
  if food.lower() == "q":
    break
  else:
    price = float(input(f"Enter the price of the {food}: $"))
    prices.append(price)
    foods.append(food)

print("-----YOUR CART-----")

for food in foods:
  print(food, end=" ")

for price in prices:
  total += price

print()
print(f"The Total cost of your cart is : ${total}")