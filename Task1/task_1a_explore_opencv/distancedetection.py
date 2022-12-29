import cv2
import numpy as np

cap = cv2.VideoCapture(0 )
while(cap.isOpened()):
		_,frame = cap.read()
		if(_ == True):
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

			lower_yellow = np.array([15, 100, 20])
			upper_yellow = np.array([30, 255, 255])

			mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)

			_,thresh1 = cv2.threshold(mask1, 250, 255, cv2.THRESH_BINARY)
			contour,heir = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

			for cont in contour:
				approx = cv2.approxPolyDP(cont,0.01*cv2.arcLength(cont,True),True)
				if(len(approx) > 10):
					area = cv2.contourArea(cont)
					M = cv2.moments(cont)
					cx = int(M["m10"] / M["m00"])
					cy = int(M["m01"] / M["m00"])
					distance = 2*(10**(-7))* (area**2) - (0.0067 * area) + 83.487
					S = 'Distance Of Object: ' + str(distance)
					cv2.putText(frame, S, (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
					cv2.drawContours(frame, cont, -1, (0,255,0), 3)
			cv2.imshow('result',frame)
			k = cv2.waitKey(10)
			if k == 27:
				break
		else:
			break

cap.release()
cv2.destroyAllWindows()