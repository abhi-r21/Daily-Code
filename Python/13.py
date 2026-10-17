#nested loops = A loop within another loop(outer , inner)
# outer loop:
#    inner loop:

rows = int(input("Enter the # no of rows: "))
columns = int(input("Enter the # no of columns: "))
symbol = input("Choose the symbol: ")

for x in range(rows):
  for y in range(columns):
    print(symbol, end="")
  print()