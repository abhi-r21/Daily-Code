# Dictionary = a collection of {key: values} pairs
# Ordered and changeable , no duplicates

capitals = {"America": "Washington D.C.", 
"India": "New Delhi",
"China": "Beijing",
"Russia": "Moscow"}

print(capitals.get("America")) #gets the value associated with the key 
capitals.update({"Germany": "Berlin"}) #We can insert new key or update the existing key 
capitals.pop("China") #we can remove the key
capitals.popitem() #Remove the item that was inserted lastest
capitals.clear() #Clears the dictonary

keys = capitals.keys() #Returns all the keys in the dictonary
for key in capitals.keys():
  print(key)

values = capitals.values() #Returns all the values in the dictonary
for value in capitals.values():
  print(value)

items = capitals.items() #Returns all the keys and values in the dictonary
for key, value in capitals.items():
  print(f"{key}: {value}")