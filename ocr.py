import cv2
import pytesseract
import numpy as np
import sendAlertEmailWithAttachment

def ocr():
    keyword = "America"

    file = "noland2.jpg"

    img = cv2.imread(file)
    #Alternatively: can be skipped if you have a Blackwhite image
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)

    kernel = np.ones((2, 1), np.uint8)
    #img = cv2.erode(gray, kernel, iterations=1) Skipping because they mess with OCR too much
    #img = cv2.dilate(img, kernel, iterations=1) Skipping because they mess with OCR too much
    out_below = pytesseract.image_to_string(img)
    if(out_below.find(keyword)>0):
        sendAlertEmailWithAttachment.sendEmail(username, file)
    print("OUTPUT:", out_below)