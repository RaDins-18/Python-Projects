# QUESTION:

# Create a python program capable of greeting you with Good Morning, Good Afternoon, Good Evening and Good Night. Your program should use time module to get the current hour.



# SOLUTION:

# Importing time module.
import time
# Set formate of time.
Time = time.strftime("%I:%M:%S:%p")
# Print time.
print("Time is", Time)

# t is equal to Time.
t = Time

# If time is between 4AM to 12AM then run below code.
if(t >= "4:00:00:AM" and t <= "11:59:59:AM"):
  # Greet Good Morning.
  print("Good Morning Sir")
# If time is between 12PM to 4PM then run below code.
elif(t >= "12:00:00:PM" and t <= "03:59:59:PM"):
  # Greet Good Afternoon.
  print("Good Afternoon Sir")
# If time is between 4PM to 8PM then run below code.
elif(t >= "04:00:00:PM" and t <= "07:59:59:PM"):
  # Greet Good Evening.
  print("Good Evening Sir")
# Time is not match above statement then run below code.
else:
  # Greet Good Night.
  print("Good Night sir")