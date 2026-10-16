#Python compound interest calculator

principle = 0
interest = 0
time = 0

while principle <= 0 :
  principle = int(input("Enter the amount you want: "))
  if principle <= 0:
   print("principle amount can't be less than or equal to 0")
  
while interest <= 0 :
  interest = float(input("Enter at how much rate of interest do you want: "))
  if interest <=0 :
    print("Interest rate can be less then or equal to 0")

while time <= 0:
  time = int(input("In how many years you will return back the money: "))
  if time <= 0:
    print("Please enter the proper time period(Time period should be >=1 ):")

TotalReturn = principle * pow((1 + interest / 100), time)
print(f"The total amount this person should return to us is ${TotalReturn: ,}") 
