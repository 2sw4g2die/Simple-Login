# Name: Lana Cossettini
# Date: 23-5-2022
# Purpose: Simple login program that allows users to login, create account, or view accounts.

import string
import random
import sys
import time

#menu
print("A: Log-in")
print("B: Create Account")
print("C: View Accounts")
print("D: Quit")
selection = input("Select: ")

print(" ")

#Log-in
if selection == "A" or selection == "a":
  print("LOG IN")
  username = input("Enter username: ")
  password = input("Enter password: ")
  f = open("accounts.txt","r")
  info = f.read().split()

  #checking username
  if username in info: 
    #identifying password index
    index=info.index(username)+1 
    user_pass=info[index]
    #checking password
    if user_pass == password:
     print("You have successfully logged in")
    else:
      print("Password incorrect, try again")
  else:
      print("User not found, try again")

#register
elif selection == "B" or selection == "b":
  print("CREATE ACCOUNT")
  username = input("create username: ")
  f = open("accounts.txt", "r")
  f = f.read().split()

  if username in f:
    print("username already exists, try again")

  #password selection
  else: 
    print("would you like to...")
    print("A: Create a password?")
    print("B: Generate a password?")
    i = input("Select: ")

    #create password
    if i == "a" or i == "A": 
      password = input("Create password: ")
      user = username + " " + password
      f = open("accounts.txt", "a") 
      f = f.write("\n" + user)

    #generate password
    if i == "b" or i == "B": 
      usedigits = input("would you like to include 'Numbers'? [Y/N] ") 
      if usedigits == "n" or usedigits == "N":
        use_digits = False
      elif usedigits == "y" or usedigits == "Y":
        use_digits = True
      else:
        print("Invalid selection, try again.")
      
      usepunctuation = input("would you like to include 'Symbols'? [Y/N] ") 
      if usepunctuation == "n" or usepunctuation == "N":
        use_punctuation = False
      elif usepunctuation == "y" or usepunctuation == "Y":
        use_punctuation = True
      else:
        ("Invalid selection, try again.")
        
      password_length = input("Length of password: ") 
      if password_length == "":
        password_length = 10
      else:
        password_length = int(password_length)

      letters = string.ascii_letters 
      digits = string.digits
      punctuation = string.punctuation 
  
      #password based off of user selections
      symbols = letters
      if use_digits:
        symbols = symbols + digits
      if use_punctuation:
        symbols = symbols + punctuation 

      #creating password
      password = "".join(random.choice(symbols) for i in range(password_length)) 
      print("Your password is: ", password)

      user = username + " " + password
      f = open("accounts.txt", "a")
      f = f.write("\n" + user) 

#view accounts
elif selection == "C" or selection == "c":
  print("ACCOUNTS")
  f = open("accounts.txt", "r")
  f = f.read()
  print(f)

#Quit
elif selection == "D" or selection == "d":
  print("exiting the program...")
  time.sleep(2)
  sys.exit()
  
else:
  print("Invalid selection, try again")
