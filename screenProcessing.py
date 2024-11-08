import pyautogui
import cv2
import easyocr
import time
import json
import numpy as np

from PIL import Image

from matplotlib import pyplot as plt





def screenshot(path):

    pyautogui.screenshot(path)
    print("Stored screenshot to: " + str(path) + " Successfully!")

def textFromImage(startRow, startColumn, width, height, debugMode):

    img = cv2.imread(r'C:\\Users\\ace\\Music\\BlindSideAI-Trevin\\BlindSideAI-py\\screenshots\\fullscreenShot.jpg')
    img = cv2.resize(img, (1920, 1080))
    if debugMode:
        cv2.imshow("original", img)
    
    # Cropping an image
    cropped_image = img[startColumn:height, startRow:width]
    
    if debugMode:
        # Display cropped image
        cv2.imshow("cropped", cropped_image)
    
    # Save the cropped image
    cv2.imwrite("screenshots\\Cropped Image.jpg", cropped_image)

    if debugMode:
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    reader = easyocr.Reader(['en'], gpu=False)

    text = reader.readtext(cropped_image)

    for i in text:
        # print(i)
        boundBox, text_, score = i
        print("Text: " + text_ + " Probability: " + str(score))
    
    return text

def updateJSON():
    with open('data\\gameStorage.json', 'w') as file:
        dictionary = {
            "gameStats": {
                "hands": 4,
                "discards": 3,
                "money": "money :D",
                "blind": blind,
                "chips": "not a feature rn... working on it",
                "hand_size": int(handData[0])
            }
        }
        jsonObj = json.dumps(dictionary, indent=4)
        file.write(jsonObj)

# time.sleep(3)

screenshot("screenshots\\fullscreenShot.jpg")

# screenshot("screenshots\\chipsShot.png", 236, 232, 235, 54)

# screenshot("screenshots\\handShot.png", 1000, 862, 90, 27)

blind = textFromImage(82, 80, 490, 145, False)

# chips = str(textFromImage())

handData = textFromImage(1021, 864, 1073, 884, False) # 1021, 864, 1073, 884
for i in handData:
    handD_bound, handD_text, handD_score = i
    handData = handD_text
handData = handData.split("/")

print(handData)

# if chips.find(','):
#     chips = chips.replace(',', '')

# updateJSON()



