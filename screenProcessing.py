import pyautogui
import cv2
import easyocr
import time
import json





def screenshot(path, x, y, width, height):

    pyautogui.screenshot(path, (x, y, width, height))
    print("Stored screenshot to: " + str(path) + " Successfully!")

def textFromImage(imgPath):
    img = cv2.imread(imgPath)
    reader = easyocr.Reader(['en'], gpu=False)

    text = reader.readtext(img)

    for i in text:
        print(i)
        boundBox, text_, score = i
        return text_

def updateJSON():
    with open('data\\gameStorage.json', 'w') as file:
        dictionary = {
            "gameStats": {
                "hands": 4,
                "discards": 3,
                "money": "money",
                "blind": blind,
                "chips": chips,
                "hand_size": int(handData[0])
            }
        }
        jsonObj = json.dumps(dictionary, indent=4)
        file.write(jsonObj)

# time.sleep(3)

# screenshot("screenshots\\bossShot.png", 75, 75, 425, 75)

# screenshot("screenshots\\chipsShot.png", 236, 232, 235, 54)

# screenshot("screenshots\\handShot.png", 1000, 862, 90, 27)

blind = textFromImage("screenshots\\bossShot.png")

chips = str(textFromImage("screenshots\\chipsShot.png"))

handData = str(textFromImage("screenshots\\handShot.png"))
handData = handData.split("/")

print(handData)

if chips.find(','):
    chips = chips.replace(',', '')

updateJSON()



