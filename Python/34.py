#Python Encrypted Program

from email import charset
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#Encrypt

plain_text = input("Enter your message: ")
cipher_text = " "

for letter in plain_text:
  index = chars.index(letter)
  cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

#Decrypt

cipher_text = input("Enter your Message: ")
plain_text = " "

for letter in cipher_text:
  index = key.index(letter)
  plain_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"original message: {plain_text}")
