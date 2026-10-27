# Match-case statement (switch): An alternative to using many 'elif' statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

def day_of_week(day):
  match day:
    case 1:
      return "It's Sunday"
    case 2:
      return "It's Monday"
    case 3:
      return "It's Tuesday"
    case 4:
      return "It's Wednesday"
    case 5:
      return "It's Thursday"
    case 6:
      return "It's Friday"
    case 7:
      return "It's Saturday"
    case _:
      return "It's Invalid"

print(day_of_week(5))

#another example:

def is_weekend(day):
  match day:
    case "saturday" | "sunday" :
      return True
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" :
      return False
    case _ :
      return False

print(is_weekend("saturday"))