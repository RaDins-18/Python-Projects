# QUESTION:

# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats.

# For example:

#  sfdsf.png --> 1.png
#   vfsf.png --> 2.png
#   this.png --> 3.png
# design.png --> 4.png
#   name.png --> 5.png



# SOLUTION:

# Importing important modules.
import string, random
import os

# Function for Generating random names.
def get_random_string(length):
  # Assign empty list.
  random_str_list = []
  # For loop for running it more than one time.
  for i in range(length):
    # Get lowercase alphabates.
    letters = string.ascii_lowercase
    # Make random name with lowercase alphabates.
    random_str = ''.join(random.sample(letters, 4))
    # Add random string at the end of random_str_list.
    random_str_list.append(random_str)
  # Return random_str_list.
  return random_str_list

# Function for making data folder.
def make_data_folder():
  # If data folder is not exists then run below block code.
  if(not os.path.exists("data")):
    # Make data folder.
    os.mkdir("data")

# Function for making pictures folder.
def make_pictures_folder():
  # If pictures folder is not exists in data folder then run below block code.
  if(not os.path.exists("data/pictures")):
    # Make pictures folder in data folder.
    os.mkdir("data/pictures")

# Function for making .png files with random name.
def make_png_files():
  # For loop for getting each name from list of random names.
  for l in list:
    # Location of files.
    path = f"data/pictures/{l}.png"
    # Write files.
    with open(path, "w"):
      pass

# Change name of .png files / clear the clutter.
def change_files_name():
  # Location of files.
  new_list = os.listdir("data/pictures")
  # For loop for getting each file from list of files.
  for i, file in enumerate(new_list, 1):
    # If file is in PNG format.
    if file.endswith(".png"):
      # Print file name.
      print(file)
      # Organize files by renaming them.
      os.rename(f"data/pictures/{file}", f"data/pictures/{i}.png")

# Declare list of random names with get_random_string() function.
list = get_random_string(5)
# Make data folder with make_data_folder() function.
make_data_folder()
# Make pictures folder with make_pictures_folder() function.
make_pictures_folder()
# Make PNG files with make_png_files() function.
# make_png_files()
# Organize files name with change_files_name() function.
change_files_name()