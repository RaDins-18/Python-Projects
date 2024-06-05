# QUESTION:

# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system like windows, linux, mac, etc.



# SOLUTION:

# Importing required modules.
from plyer import notification
import time

# While loop for running script repeatedly.
while True:
    # Use notify function from notification module and set argumrnts for pop-up notification.
    notification.notify(
        # Set title of notification.
        title = "It's a request!",
        # Set message of notification.
        message = 'Hey your body needs water.\nSo, take it.',
        # Set icon of notification.
        app_icon = "icon.ico",
        # Set 10s stay for notification.
        timeout = 10,
        # Set toast.
        toast = False
    )
    # 1 hour delay after every notification.
    time.sleep(3600)