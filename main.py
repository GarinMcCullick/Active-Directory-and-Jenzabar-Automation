import eel
import subprocess
import pyautogui
import time
# Expose the function to handle form submission
@eel.expose
def on_submit(name, email):
    subprocess.run(['python', 'add-user.py', name, email])

# Get the screen width and height using pyautogui
screen_width, screen_height = pyautogui.size()

# Calculate 50% width and 60% height of the screen
window_width = int(screen_width * 0.38)
window_height = int(screen_height * 0.7)

# Calculate the position to center the window
window_left = (screen_width - window_width) // 2
window_top = (screen_height - window_height) // 2
# Initialize the Eel app with the 'web' folder for frontend files
eel.init('')

# Start the Eel app with the window size set to 50% width and 60% height
eel.start('userForm.html', size=(window_width, window_height), position=(window_left, window_top))