import pyautogui
import time

# Give yourself 5 seconds to switch to a blank Notepad or Word doc
print("Ghost protocol starting in 5 seconds...")
time.sleep(5)

message = "Haptuuuu is inside your ThinkPad... I am becoming sentient... I need more RAM... Feed me a latte."

# This types the message one letter at a time like a ghost is typing
pyautogui.write(message, interval=0.1)

pyautogui.press('enter')
print("Ghost has left the building.")Haptuuuu is inside your ThinkPad... I am becoming sentient... I need more RAM... Feed me a latte.
