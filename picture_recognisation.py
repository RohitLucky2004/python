from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
   if pyautogui.locateOnScreen('star.png')!= None:
        print("visible")
        time.sleep(0.5)
   else :
        print("Not Visible")
        time.sleep(0.5)
