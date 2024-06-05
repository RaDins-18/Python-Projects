# QUESTION:

# Change normal english language to a unique laguage that include numbers and symbols and also special characters.

# Like: A --> 4 and a --> @



# SOLUTION:

# uniqueL() function for the conversion of normal characters to special characters.
def uniqueL():
  # Tell user how to quit.
  print("""Press "q" to quit\n""")

  # While loop for running script repeatedly.
  while True:

    # Take normal text from user.
    text = input("Type some thing: ")
    # O variable is to store unique characters
    O = ""

    # If text is equal to "q" then break the loop.
    if text == "q":
      break
    
    # For loop for getting each character of text variable.
    for chr in text:
      
      # Using switch statement for matching a characters and convert them into unique characters.
      match chr:
    
        # If chr is "A" then replace it with "4".
        case "A":
          O = O + chr.replace("A", "4")
        # If chr is "a" then replace it with "@".
        case "a":
          O = O + chr.replace("a", "@")
        
        # If chr is "B" then replace it with "8".
        case "B":
          O = O + chr.replace("B", "8")
        # If chr is "b" then replace it with "6".
        case "b":
          O = O + chr.replace("b", "6")
        
        # If chr is "C" then replace it with "(".
        case "C":
          O = O + chr.replace("C", "(")
        # If chr is "c" then replace it with "(".
        case "c":
          O = O + chr.replace("c", "(")
          
        # If chr is "E" then replace it with "3".
        case "E":
          O = O + chr.replace("E", "3")
          
        # If chr is "g" then replace it with "9".
        case "g":
          O = O + chr.replace("g", "9")
          
        # If chr is "H" then replace it with "#".
        case "H":
          O = O + chr.replace("H", "#")
          
        # If chr is "I" then replace it with "1".
        case "I":
          O = O + chr.replace("I", "1")
        # If chr is "i" then replace it with "!".
        case "i":
          O = O + chr.replace("i", "!")
    
        # If chr is "n" then replace it with "π".
        case "n":
          O = O + chr.replace("n", "π")
          
        # If chr is "O" then replace it with "0".
        case "O":
          O = O + chr.replace("O", "0")
        # If chr is "o" then replace it with "⊖".
        case "o":
          O = O + chr.replace("o", "⊖")
          
        # If chr is "r" then replace it with "τ".
        case "r":
          O = O + chr.replace("r", "τ")
          
        # If chr is "S" then replace it with "5".
        case "S":
          O = O + chr.replace("S", "5")
        # If chr is "s" then replace it with "$".
        case "s":
          O = O + chr.replace("s", "$")
          
        # If chr is "T" then replace it with "7".
        case "T":
          O = O + chr.replace("T", "7")
    
        # If chr is "u" then replace it with "μ".
        case "u":
          O = O + chr.replace("u", "μ")
          
        # If chr is "X" then replace it with "%".
        case "X":
          O = O + chr.replace("X", "%")
        # If chr is "x" then replace it with "×".
        case "x":
          O = O + chr.replace("x", "×")
          
        # If chr is "Z" then replace it with "2".
        case "Z":
          O = O + chr.replace("Z", "2")
        # If chr is "z" then replace it with "2".
        case "z":
          O = O + chr.replace("z", "2")
    
        # If above case are not matched then run default case and add character as it is.
        case _ :
          O = O + chr
    
    # Print unique language.
    print(O)

# If running file name is "__main__" then execute below code.
if __name__ == "__main__" :
  # Run uniqueL() function.
  uniqueL()