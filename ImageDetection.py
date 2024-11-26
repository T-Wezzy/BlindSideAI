import pyautogui
import cv2
import easyocr
import numpy as np

class DetectHand:


    def __init__(self):
        self.hand = []

    def screenshot(path):
        pyautogui.screenshot(path)
        print("Stored screenshot to: " + str(path) + " Successfully!")

    def getHandSize(self, debugMode):

        img = cv2.imread(r'C:\\Users\\ace\\Music\\BlindSideAI-Trevin\\BlindSideAI-py\\screenshots\\fullscreenShot.jpg')
        img = cv2.resize(img, (1920, 1080))
        if debugMode:
            cv2.imshow("original", img)

        # Cropping an image
        cropped_image = img[864:884, 1021:1073]

        if debugMode:
            # Display cropped image
            cv2.imshow("cropped", cropped_image)

        # Save the cropped image
        cv2.imwrite("screenshots\\croppedShot.jpg", cropped_image)

        if debugMode:
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        reader = easyocr.Reader(['en'], gpu=False)

        text = reader.readtext(cropped_image)

        for i in text:
            # print(i)
            boundBox, text_, score = i
            print("Text: " + text_ + " Probability: " + str(score))

        return text_[0]
    
    def detectHandLogic(self):
        img = cv2.imread(r'C:\\Users\\ace\\Music\\BlindSideAI-Trevin\\BlindSideAI-py\\screenshots\\fullscreenShot.jpg')
        img = cv2.resize(img, (1920, 1080))

        # Cropping an image
        cropped_image = img[864:884, 1021:1073]
        
        if self.getHandSize()[0] == "8":
            pyautogui.moveTo(615, 753)
            img_rgb = cv2.imread('screenshots\\fullscreenShot.jpg')
            template = cv2.imread('data\\reference\\AceOfHearts.jpg')
            w, h = template.shape[:-1]

            res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
            threshold = .8
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):  # Switch columns and rows
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

            cv2.imwrite('result.png', img_rgb)