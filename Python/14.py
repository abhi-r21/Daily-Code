#collection = single "variable" used to store mutliple values
#   List = [] ordered and changeable, Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK, no Duplicates
#   Tuple = () ordered and unchangeable, Duplicates OK. Faster 


fruits = ["apple", "banana", "mango", "pineapple" ]
print(len(fruits)) #find the length of the list
print("pineapple" in fruits) #check whether the item is in list , true or false

fruits[0] = "Muskmelon" #changes the items in specified index num
fruits.append("WaterMelon")#adds item to the list 
fruits.remove("apple")#removes the item from list
fruits.insert(0, "papaya")# adds the items in a specific index
fruits.sort()# sort the items in alphabetical order
fruits.reverse()#reverses the items
fruits.clear()#clears the list

print(fruits)#prints the list
print(fruits.index("apple"))#prints the index of the specific item 
print(fruits.count("apple"))#prints how many times is repeated or duplicated
