from pyautogui import * 
import pyautogui 
import time 


while 1:
    if pyautogui.locateOnScreen('Lock.png', confidence=0.5) != None:
        print("Unlocked")
        time.sleep(0.5)
    else:
        print("Not Located")
        time.sleep(0.5)
