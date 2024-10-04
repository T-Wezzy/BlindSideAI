import pyautogui
import keyboard

def mousePos():
    mouseX, mouseY = pyautogui.position()
    return "Mouse Posistion: (" + str(mouseX) + ", " + str(mouseY) + ")"



while True:
    try:
        if keyboard.is_pressed('space'):
            print(mousePos())
            break
    except:
        break