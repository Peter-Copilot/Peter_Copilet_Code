import keyboard
import time
import pyautogui
import sys

pyautogui.PAUSE = 0.3
click = False

if keyboard.wait(hotkey='F4+t') == None:
    click = True

i = 0
try:
    while click == True and i < 1000:
        pyautogui.click(button = 'right')
        i = i + 1

except KeyboardInterrupt:
    sys.exit(0)
    
##    if keyboard.wait(hotkey='ctrl+shift') == None:
##        click = False

    
