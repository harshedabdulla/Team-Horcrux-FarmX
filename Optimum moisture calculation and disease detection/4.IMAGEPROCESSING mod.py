# Python code for Multiple Color Detection


import numpy as np
import cv2,csv
import os,time


# Capturing video through webcam
webcam = cv2.VideoCapture(0)

def put1 (a):
	with open("QINDEX.csv",mode='w') as csvfile :	 #feeding each values to csv
		mywriter=csv.writer(csvfile)
		mywriter.writerow([int(a)]) 
		csvfile.close()
		print("done")

# Start a while loop
while(1):

	yellowarea=float(0.0)
	greenarea=float(0.0) 
	ygare=float(0.0)
	brownarea=float(0.0)
	bluearea=float(0.0)
	# Reading the video from the
	# webcam in image frames
	_, imageFrame = webcam.read()

	# Convert the imageFrame in
	# BGR(RGB color space) to
	# HSV(hue-saturation-value)
	# color space
	#hsvFrame = cv2.resize(imageFrame, (500, 250))
	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)


	# Set range for green color and
	# define mask
	green_lower = np.array([36, 50, 70], np.uint8)
	green_upper = np.array([89, 255, 255], np.uint8)
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

	yellow_lower = np.array([23, 41, 133], np.uint8)
	yellow_upper = np.array([40, 150, 255], np.uint8)
	yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

	brown_lower = np.array([10.625, 76.5, 68.85], np.uint8)
	brown_upper = np.array([15.83,127.5, 153.5], np.uint8)
	brown_mask = cv2.inRange(hsvFrame, brown_lower, brown_upper)

	blue_lower = np.array([110, 50, 50], np.uint8)
	blue_upper = np.array([130, 255, 255], np.uint8)
	blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

	black_lower = np.array([0, 0, 0], np.uint8)
	black_upper = np.array([180, 255, 30], np.uint8)
	black_mask = cv2.inRange(hsvFrame, black_lower, black_upper)


	imageFrame[np.where(green_mask == 0)] = 0
	imageFrame[np.where(yellow_mask > 0)] = (0, 255, 255)
	imageFrame[np.where(brown_mask > 0)] = (0, 0, 255)
	imageFrame[np.where(blue_mask > 0)] = (0, 0, 255)
	imageFrame[np.where(black_mask > 0)] = (0, 0, 255)
	# Program Termination

	cv2.imshow("dfsdf", imageFrame)

	greenarea = cv2.countNonZero(green_mask)
	yellowarea = cv2.countNonZero(yellow_mask)
	brownarea = cv2.countNonZero(brown_mask) + cv2.countNonZero(blue_mask)+cv2.countNonZero(black_mask) 
	print(greenarea)
	print(yellowarea)
	print(brownarea)
	if yellowarea ==0:
		yellowarea = yellowarea+1

	if brownarea ==0:
		brownarea = 1

	if greenarea ==0:
		greenarea = 1
	#print(brownarea/yellowarea)
	if brownarea/yellowarea >1 and brownarea > 300:
		print("LEAF MIGHT HAVE DISEASE")
		time.sleep(1)
		os.system("cls")
		put1(6)
	elif yellowarea/greenarea >.07 and yellowarea>3000 :
		print("LEAF HAS MOISTURE PROBLEM")
		put1(3)
		time.sleep(0.1)
		os.system("cls")
	
	elif greenarea<10000 and yellowarea <3000  :
		print("no leaf")
		put1(0)
		time.sleep(0.1)
		os.system("cls")
	else:
		print("LEAF IS HEALTHY")
		put1(5)
		time.sleep(0.1)
		os.system("cls")




	
	

	
	

	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
	


