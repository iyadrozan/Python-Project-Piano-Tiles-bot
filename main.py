from pyautogui import *
import pyautogui
import time
import keyboard
import random
from win32 import win32api, win32console

# Tile 1 Position: X: 1198 Y: 675 RGB: ( 77, 80, 115)
# Tile 1 Position: X: 1038 Y: 675 RGB: ( 77, 80, 115)
# Tile 1 Position: X: 882 Y: 675 RGB: ( 77, 80, 115)
# Tile 1 Position: X: 717 Y: 675 RGB: ( 77, 80, 115)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32console.MOUSE_EVENT,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32console.MOUSE_EVENT,0,0)
    
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(1198, 675) [0] == 0:
        click(1198, 675)
    if pyautogui.pixel(1038, 675) [0] == 0:
        click(1038, 675)
    if pyautogui.pixel(882, 675) [0] == 0:
        click(882, 675)
    if pyautogui.pixel(717, 675) [0] == 0:
        click(717, 675)