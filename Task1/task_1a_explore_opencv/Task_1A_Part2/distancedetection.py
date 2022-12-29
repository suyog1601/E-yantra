import cv2
import numpy as np
cap = cv2.VideoCapture('ballmotion.mp4')
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.get(4))


while(cap.isOpened()):
  _,frame = cap.read()
  if(_ == True):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 230, 120])
    upper_red = np.array([10, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    _,thresh1 = cv2.threshold(mask1, 250, 255, cv2.THRESH_BINARY)

    contour,heir = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cont in contour:
      approx = cv2.approxPolyDP(cont,0.01*cv2.arcLength(cont,True),True)
      if(len(approx) > 9):
        cv2.drawContours(frame, cont, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()
