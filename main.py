from control_trials import ControlGame
from grayscale import Grayscale
from time import time
from window_capture import WindowCapture
from write_inputs import WriteInputs
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os
import pyautogui,time
import threading

def rewrite():
	threading.Timer(6.0, rewrite).start()
	f = open("./Trials-TAS-Tool/Scripts/TAS.txt", "r")
	print(f.read())
	writer = WriteInputs()
	writer.write()
	pyautogui.press('r')

def main():
	rewrite()
	
	# initialize the WindowCapture class
	trials = WindowCapture('Trials Fusion')

	ControlGame()

	while(True):
		#loop_time = time()
		# Get an updated image of the game every frame
		screenshot = trials.get_screenshot()	
		# grayscale = Grayscale()
		# grayscale.find_marker(screenshot)

		# # path 
		# path = r'./template_img.png'
		
		# # Reading an image in default mode
		# src = cv.imread(path)

		# Convert stream of images (video) into grayscale one by one
		grayImg = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
		ret, thresh = cv.threshold(grayImg, 110, 255, cv.THRESH_BINARY)

		# Find & Draw contours of image
		contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
	

		X = [c[0] for c in [b[0] for b in [a[0] for a in contours]]]
		Y = [c[1] for c in [b[0] for b in [a[0] for a in contours]]]

		# print(Y)
		# print(Y)
		# # plot our list in X,Y coordinates
		plt.scatter(X,Y)
		plt.show()
				

		# BEN UNCOMMENT THESE FOR CONTOURS
		# for i in range(len(contours)):
		# 	cv.drawContours(src, contours[2], -1, (0,255,0), 3)
		# 	input("Press enter to continue")
		# 	cv.imshow('Computer Vision', src)
		# 	cv.waitKey(1)
			
		# cv.drawContours(screenshot, contours, -1, (0,255,0), 3)
		# cv.imshow('Computer Vision', screenshot)

		# Display stream of images with contours
		


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