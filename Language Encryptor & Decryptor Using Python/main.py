# QUESTION:

# Write a python program to translate a message into secret encrypted language. Use the rules below to translate normal English into secret encrypted language.

# Rules Of Encrypting:
# • If the word contains 1 character, add two random characters at start of word and two random characters at end of word.
# • If the word contain 2 characters, reverse the word then add two random characters at start of word and two random characters between word.
# • If the word contain 3 or more characters, reverse the word then remove two starting characters of word and add it at the end of word then add three random characters at the starting of word and also 3 random characters at the end of word.

# Rules Of Decrypting:
# • If the word contains 5 character, remove two random characters at start of word and two random characters at end of word.
# • If the word contain 6 characters, remove two random characters at start of word and two random characters between word [1:3] then reverse the word.
# • If the word contain 6 or more characters, remove three random characters at the starting of word and also 3 random characters at the end of word then remove two ending characters of word and add it at the starting of the word and lastly reverse the word.

# Your program should ask whether you want to encrypt or decrypt.



# SOLUTION:

# Importing important modules.
import random
import string

# Get message from user.
message = input(str("Enter a message: "))
# Convert message to lowercase.
message = message.lower()

# If message contain number or numbers then execute only if block code.
if(message.isnumeric() == True):
  # Tell user that numbers are not allowed.
  print("Type only alphabates!")
  
# If number does not contain any number then execute below code.
else:
  # Take user choise between encryption or decryption.
  userChoice = input("What you want encrypt (e) / decrypt (d): ")
  
  # Encryption:
  # If user choose encrytion.
  if(userChoice == "e"):
    
    # Make an empty encrypt variable.
    encrypt = ""
    
    # If length of message is 0 to 2 then run below if block code.
    if len(message) in range(0, 3):
      # Reverse the characters.
      reverseTheChr = message[::-1]
      
      # Add it into encrypt variable.
      encrypt = reverseTheChr
      
      # Print ecrypted message.
      print("Encrypted:", encrypt)
      
    # If length of message is greater than 2 then run below else block code.
    else:
      # For loop for take each word of message.
      for i in message.split():
        
        # If length of word is equal to 1 then run below if block code.
        if(len(i) == 1):
          # finalResult variable is equal to i variable.
          finalResult = i
          
          # Get lowercase alphabets.
          letters = string.ascii_lowercase
          # Get 2 random characters by lowercase alphabets.
          add2Chr_1 = ''.join(random.sample(letters, 2))
          # Get 2 more random characters by lowercase alphabets.
          add2Chr_2 = ''.join(random.sample(letters, 2))

          # Add all things in the encrypt variable.
          encrypt = encrypt + add2Chr_1 + finalResult + add2Chr_2 + " "
        
        # If length of word is equal to 2 then run below elif block code.
        elif(len(i) == 2):
          # Reverse the characters.
          reverseTheChrs = i[::-1]
          
          # finalResult variable is equal to reverseTheChrs variable.
          finalResult = reverseTheChrs
    
          # Get lowercase alphabets.
          letters = string.ascii_lowercase
          # Get 2 random characters by lowercase alphabets.
          add2Chr_1 = ''.join(random.sample(letters, 2))
          # Get 2 more random characters by lowercase alphabets.
          add2Chr_2 = ''.join(random.sample(letters, 2))
        
          # Add all things in the encrypt variable.
          encrypt = encrypt + add2Chr_1 + finalResult[0] + add2Chr_2 + finalResult[1] + " "
        
        # If length of word is 3 or greater than 3 then run below else block code.
        else:
          # Reverse the characters.
          reverseTheChrs = i[::-1]
          
          # Add 2 starting characters of word at the end of word.
          addChrAtLast = ''.join((reverseTheChrs, reverseTheChrs[0:2]))
          
          # Remove 2 starting characters of word.
          removeChrAtStart = addChrAtLast.replace(reverseTheChrs[0:2], "", 1)
    
          # finalResult variable is equal to removeChrAtStart variable.
          finalResult = removeChrAtStart
        
          # Get lowercase alphabets.
          letters = string.ascii_lowercase
          # Get 2 random characters by lowercase alphabets.
          add3Chr_1 = ''.join(random.sample(letters, 3))
          # Get 2 more random characters by lowercase alphabets.
          add3Chr_2 = ''.join(random.sample(letters, 3))
          
          # Add all things in the encrypt variable.
          encrypt = encrypt + add3Chr_1 + finalResult + add3Chr_2 + " "
    
      # Print ecrypted message.
      print("Encrypted:", encrypt)
  
  # Decryption:

  elif(userChoice == "d"):

    # Make an empty decrypt variable.
    decrypt = ""
    
    # If length of message is 0 to 2 then run below if block code.
    if len(message) in range(0, 3):
      # Reverse the characters.
      reverseTheChr = message[::-1]
      
      # Add it into decrypt variable.
      decrypt = reverseTheChr
      
      # Print decrypted message.
      print("Decrypted:", decrypt)
      
    # If length of message is greater than 2 then run below else block code.
    else:
      # For loop for take each word of message.
      for i in message.split():

        # If length of word is equal to 5 then run below if block code.
        if(len(i) == 5):
          # Get only 3rd character of word.
          chr = i[2]
          
          # finalResult variable is equal to chr variable.
          finalResult = chr
    
          # Add all things in the decrypt variable.
          decrypt = decrypt + finalResult + " "
          
        # If length of word is equal to 6 then run below elif block code.
        elif(len(i) == 6):
          # Get 3rd character of word.
          firstLetter = i[2]
          
          # Get last character of word.
          secondLetter = i[5]

          # Add firstLetter variable with secondLetter variable and assign them by add2Chr variable.
          add2Chr = firstLetter + secondLetter
          
          # Reverse the characters.
          reverseTheChrs = add2Chr[::-1]
          
          # finalResult variable is equal to reverseTheChrs variable.
          finalResult = reverseTheChrs

          # Add all things in the decrypt variable.
          decrypt = decrypt + finalResult + " "
        
        # If length of word is greater than 6 then run below else block code.
        else:
          # Remove 3 characters from starting and end of the word.
          remove3Chrs = i[3:-3]
      
          # Reverse the characters.
          reverseTheChrs = remove3Chrs[::-1]

          # Add 2 starting characters at the last of word.
          addChrAtLast = ''.join((reverseTheChrs, reverseTheChrs[0:2]))
          
          # Remove 2 starting characters of the word.
          removeChrAtStart = addChrAtLast.replace(reverseTheChrs[0:2], "", 1)
          
          # finalResult variable is equal to removeChrAtStart variable.
          finalResult = removeChrAtStart
      
          # Add all things in the decrypt variable.
          decrypt = decrypt + finalResult + " "

      # Print decrypted message.
      print("Decrypted:", decrypt.capitalize())