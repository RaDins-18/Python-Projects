# QUESTION:

# Write a python program that can get info of a employee and make a info card.
# Card is like Abuzar_Alvi.png image.



# SOLUTION:

# Importing important modules.
from PIL import Image, ImageDraw, ImageFont, ImageOps
from textwrap import fill

# main() function that generates info card.
def main():
    # Assign background variable with backgroung file.
    background = Image.open("resources/background.png").convert("RGBA")
  
    # Take name and assign it with rawName variable.
    rawName = input("Name: ")
    # Modify rawName variable and assign it with name variable.
    name = rawName.replace(" ", "\n")

    # Take pic file name and assign it with rawPic variable.
    rawPic = input("Pic file name: ")
    # Modify rawPic variable and assign it with pic variable.
    pic = Image.open(f"profile-pics/{rawPic}").convert("RGBA")
   
    # Take joining year and assign it with joiningYear variable.
    joiningYear = input("Joining year: ")
    
    # Take age and assign it with age variable.
    age = int(input("Age: "))
    
    # Take rawAddress and assign it with rawAddress variable.
    rawAddress = input("Address: ")
    # Modify rawAddress variable and assign it with address variable.
    address = fill(rawAddress, width=22)
      
    # Take number and assign it with number variable.
    number = int(input("Number: "))
      
    # Take job role and assign it with role variable.
    role = input("Job role: ")

    # Assign info1 with joining year.
    info1 = f"Joined at: {joiningYear}"
    # Assign info2 with age, address, number, role.
    info2 = f"Age: {age}\n\nAddress: {address}\n\nNumber: {number}\n\nRole: {role}"

    # Assign fonts with specific font size.
    font = ImageFont.truetype(font='resources/copperplate-32-bc.ttf', size=150)
    font1 = ImageFont.truetype(font='resources/alice-regular.ttf', size=110)
    font2 = ImageFont.truetype(font='resources/alice-regular.ttf', size=95)

    # Resize image to a square.
    img = ImageOps.fit(pic, (490, 490))

    # Create circular mask.
    mask = Image.new('L', (490, 490), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 490, 490), fill=255)
  
    # Apply mask to image.
    img.putalpha(mask)

    # Get background as a canvas to draw info and attach pic on it.
    draw = ImageDraw.Draw(background)

    # If length of first name is 1 to 2 then add name at below position.
    if(len(rawName.split(" ")[0]) in [1, 2]):
        draw.text((380.4488189, 220.64566929), name, font=font, align="center", fill=(166, 166, 166), spacing= -40)

    # If length of first name is 3 to 4 then add name at below position.
    elif(len(rawName.split(" ")[0]) in [3, 4]):
        draw.text((340.4488189, 220.64566929), name, font=font, align="center", fill=(166, 166, 166), spacing= -40)

    # If length of first name is 5 then add name at below position.
    elif(len(rawName.split(" ")[0]) == 5):
        draw.text((280.4488189, 220.64566929), name, font=font, align="center", fill=(166, 166, 166), spacing= -40)

    # If length of first name is 6 then add name at below position.
    elif(len(rawName.split(" ")[0]) == 6):
        draw.text((240.4488189, 220.64566929), name, font=font, align="center", fill=(166, 166, 166), spacing= -40)

    # If length of first name is 7 then add name at below position.
    elif(len(rawName.split(" ")[0]) == 7):
        draw.text((210.4488189, 220.64566929), name, font=font, align="center", fill=(166, 166, 166), spacing= -40)

    # If length of first name is 8 then add name at below position.
    elif(len(rawName.split(" ")[0]) == 8):
        draw.text((170.4488189, 220.64566929), name, font=font, align="center", fill=(166, 166, 166), spacing= -40)

    # If length of first name is 9 then add name at below position.
    elif(len(rawName.split(" ")[0]) == 9):
        draw.text((120.4488189, 240.64566929), name, font=font, align="center", fill=(166, 166, 166), spacing= -40)

    # Add info1 at below position on background.
    draw.text((190.4488189, 620.83464567), info1, font=font1, fill=(166, 166, 166))

    # Add info2 at below position on background.
    draw.text((150.4488189, 900.59055118), info2, font=font2, fill=(166, 166, 166), spacing=10)

    # Attach pic to background.
    background.alpha_composite(img, (1012, 208))

    # Show results.
    background.show()

    # Save result.
    background.save(f"result/{rawName.replace(" ", "_")}.png")
 
#  If running file name is __main__ then run main() function.
if __name__ == '__main__':
    # Run main() function.
    main()