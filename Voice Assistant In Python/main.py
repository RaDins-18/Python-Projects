# QUESTION:

# Write a program to pronounce list of names using any module you want. If you are given a list l as follows:

# l = ["RaDin", "Larra", "Eliza"]
# Your program should pronouce:

# • Hello RaDin
# • Hello Larra
# • Hello Eliza
# Note: If you are not using windows, try to figure out how to do the same thing using some other package



# SOLUTION:

# Importing required modules.
from gtts import gTTS
import os

# List of names.
names = ["RaDin", "Larra", "Eliza", "John", "Bruce"]

# Para function return a script that we want to pronounce.
def script(list):
  # Declare empty string variable text.
  script = ""
  # For loop for getting each name from names list.
  for c in list:
    # Add hello before name.
    script = script + f"Hello {c}.\n"
  # Return script.
  return script

# # Print the script.
# print(script(names))

# Declare mytext variable with the script that you want to convert to audio.
mytext = script(names)

# Define language in which you want in audio.
language = 'en'

# Passing necessary arguments to gTTs function, So that they generate audio.
audio = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the audio file with welcome.mp3 name.
audio.save("welcome.mp3")
  
# Playing the audio file.
os.system("start welcome.mp3")