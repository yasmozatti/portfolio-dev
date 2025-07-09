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
drawColor = (0, 0, 0)
brushThickness = 15
eraserThickness = 60

cap = cv2.VideoCapture(0)  # Alterado para câmera 0
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.65, maxHands=1)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = detector.fingersUp()

        if fingers[1] and fingers[2]:
            print("Selection Mode")
            if y1 < 125:
                if 250 < x1 < 450:
                    header = overlayList[0]
                    drawColor = (0, 217, 215)
                elif 550 < x1 < 750:
                    header = overlayList[1]
                    drawColor = (159, 95, 159)
                elif 800 < x1 < 950:
                    header = overlayList[2]
                    drawColor = (255, 20, 0)
                elif 1050 < x1 < 1200:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

        elif fingers[1] and not fingers[2]:
            print("Drawing Mode")
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1

    # Merge drawings
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # Add header
    img[0:125, 0:1280] = header

    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF

    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
        break

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()