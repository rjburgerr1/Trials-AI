# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2
def find_marker(image):
	# convert the image to grayscale, blur it, and detect edges
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)
	# find the contours in the edged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv2.contourArea)
	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)


commands = ["gas", "brake", "lean", "speed"]


def formatInputs(frame, command, value):
	return f"{frame} {command} {value}"

def write():
	# TAS file format is as follows:
	# 	[frame] [command] [value] 
	# ------------------------------------------------------------------------------------------
	# 0 gas 5 # this is a comment
	# 0 lean 2
	# 10 brake 3
	# 13 brake 0 
	# 50 lean -3 # slide
	# 100 lean 0
	# 150 gas 0 # brake bounce at 2.5s
	# ------------------------------------------------------------------------------------------
	# You can also write comments in the input file. Either separate them with a space and '#' at the end of the line or in a new line starting with '#'
	# Frame can be any integer from 0 to 108000. The game has 60 frames a second, so e.g command gas 0 at 150 happened at 2.5s in-game time.
	# Command can be lean, gas, brake, speed
	# Possible values for every command: 
	# lean: -3, -2, -1, 0, 1, 2, 3. Negative values move the analog stick to the left, positive - to the right and zero basically centers the stick
	# gas: 0, 1, 2, 3, 4, 5, 6, 7. 
	# brake: 0, 1, 2, 3.
	# speed: any float value from 0 to 100

	f = open("./Trials-TAS-Tool/Scripts/TAS.txt",  "w")
	f.write(formatInputs(0, "gas", 7))
	f.close()

	f = open("./Trials-TAS-Tool/Scripts/TAS.txt", "r")
	print(f.read())

	

write()


