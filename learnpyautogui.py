import pyautogui as pg
import time as t
import keyboard as k

clicking = False

def switch():
    global clicking
    clicking = not clicking
    if clicking:
        print('clicking')
    else:
        print('not clicking')

k.add_hotkey('f7',switch)

while True:
    if clicking: #if clicking == True
        pg.click(pg.position())
        t.sleep(0.1)