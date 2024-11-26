import pyautogui
import cv2
import easyocr
import time
import json
import numpy as np

from PIL import Image

from matplotlib import pyplot as plt

import HandLogic
import ImageDetection




# time.sleep(3)

ImageDetection.DetectHand().screenshot("screenshots\\fullscreenShot.jpg")

playedHand = HandLogic.PlayedHand(["A", "K", "Q", "J", "9", "8", "2", "2"], [""])

playedHand.printLogicalResponse()

# if chips.find(','):
#     chips = chips.replace(',', '')

# updateJSON()



