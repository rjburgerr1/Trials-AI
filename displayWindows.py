import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os
from time import time
from windowCapture import WindowCapture
from grayscale import Grayscale

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath("./")))


# initialize the WindowCapture class
wincap = WindowCapture('Trials Fusion')


loop_time = time()
while(True):
		# get an updated image of the game
		screenshot = wincap.get_screenshot()	
		grayscale = Grayscale()
		grayscale.find_marker(screenshot)
		# cv.imshow('Computer Vision', screenshot)

		# img = cv.imread(screenshot)
		# plt.imshow(screenshot, cmap = 'gray', interpolation = 'bicubic')
		# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
		# plt.show()
		# debug the loop rate
		print('FPS {}'.format(1 / (time() - loop_time)))
		loop_time = time()

		# press 'q' with the output window focused to exit.
		# waits 1 ms every loop to process key presses
		if cv.waitKey(1) == ord('q'):
			cv.destroyAllWindows()
			break

print('Done.')