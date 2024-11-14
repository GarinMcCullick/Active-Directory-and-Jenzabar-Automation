import eel
import subprocess
import pyautogui

# Expose the function to handle form submission
@eel.expose
def on_submit(firstname, initial, lastname, password, login_name, email, jenzabar_id, department):
    # Call the external Python script with the user data as arguments
    subprocess.run([
        'python', 'add-user.py', 
        firstname, initial, lastname, password, 
        login_name, email, jenzabar_id, department
    ])

# Get the screen width and height using pyautogui
screen_width, screen_height = pyautogui.size()

# Calculate 38% width and 70% height of the screen (custom dimensions)
window_width = int(screen_width * 0.38)
window_height = int(screen_height * 0.7)

# Calculate the position to center the window
window_left = (screen_width - window_width) // 2
window_top = (screen_height - window_height) // 2

# Initialize the Eel app with the 'web' folder for frontend files
eel.init('web')

# Start the Eel app with the window size set to custom width and height
eel.start('userForm.html', size=(window_width, window_height), position=(window_left, window_top))
