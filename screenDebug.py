import pyautogui
import keyboard
import time

import played_hand

def mousePos():
    mouseX, mouseY = pyautogui.position()
    return "Mouse Posistion: (" + str(mouseX) + ", " + str(mouseY) + ")"


running = True
loops = 1

while loops >= 0:
    try:
        if keyboard.is_pressed('space'):
            print(mousePos())
            time.sleep(0.2)
            loops -= 1
            continue
    except:
        continue   