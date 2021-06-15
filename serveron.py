from time import time
import pyautogui
import webbrowser
from time import sleep

webbrowser.open_new_tab('https://www.aternos.org/server')


sleep(7)
def start(): 
 cords = pyautogui.locateCenterOnScreen('start.PNG') 
 pyautogui.click(cords)

start()
