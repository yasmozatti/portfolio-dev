import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath = "WebCam_Brush/header"
myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

header = overlayList[0]

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.85)

while True:
    # 1.Importing image
    sucess, img = cap.read()
    img = cv2.flip(img, 1)

    #2. Find Hands Landmarks
    img = detector.findHands(img)
    lmList = detector.findHands(img, draw=False)
    if len(lmList !=0):
        #tip of index and middle finger
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
    
    #3. Check which fingers are up
    fingers = detector.fingersUp()
    print(fingers)

    #4. If selecion mode - two fingers up (not draw)


    #5. If Drawing Mode - Index finger is up (draw)


    #Setting the header image
    img[0:125, 0:1280] = header
    cv2.imshow("Image", img)
    cv2.waitKey(1)