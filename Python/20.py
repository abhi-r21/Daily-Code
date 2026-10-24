import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number = random.randint(low, high) #returns random number btw low and high
number = random.random() #returns random floating number
option = random.choice(options) #returns random element in the options tupple
random.shuffle(cards)#returns to shuffle the items.

print()

