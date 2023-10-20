from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_eventnt(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('s')==False:
    pic = pyautogui.screenshot(region=(660,350,600,400))
    width,height=pic.size
    for i in range(0,width,5):
        for j in range(0,height,5):
            r,g,b=pic.getpixel((i,j))
            if b==195:
                click(i+660,j+350)
                time.sleep(0.005)
                break
