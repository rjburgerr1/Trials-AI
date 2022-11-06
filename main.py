from control_trials import ControlGame
from grayscale import Grayscale
from time import time
from window_capture import WindowCapture
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
	# initialize the WindowCapture class
	trials = WindowCapture('Trials Fusion')

	ControlGame()

	while(True):
		loop_time = time()
		# Get an updated image of the game every frame
		screenshot = trials.get_screenshot()	
		# grayscale = Grayscale()
		# grayscale.find_marker(screenshot)

		# Convert stream of images (video) into grayscale one by one
		grayImg = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
		ret, thresh = cv.threshold(grayImg, 127, 255, 0)

		# Find & Draw contours of image
		contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

		print(len(contours))
		cv.drawContours(screenshot, contours, -1, (0,255,0), 3)
	
		# Display stream of images with contours
		cv.imshow('Computer Vision', screenshot)

		# Debug the loop rate
		#print('FPS {}'.format(1 / (time() - loop_time)))
		
		# press 'q' with the output window focused to exit.
		# waits 1 ms every loop to process key presses
		if cv.waitKey(1) == ord('q'):
			cv.destroyAllWindows()
			break

	print('Done.')

if __name__ == "__main__":
    main()