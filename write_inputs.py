# import the necessary packages
from imutils import paths
import math
import random
import numpy as np
import imutils
import cv2

class WriteInputs:

	def write(self):

		commands = ["gas", "brake", "lean", "speed"]
		maxSpeed = 100
		leans = [-3, -2, -1, 0, 1, 2, 3]
		brakes = [0, 1, 2, 3]
		gas = [0, 1, 2, 3, 4, 5, 6, 7]

	

		def randomValFromArray(array):
			randomValue = array[math.floor(random.random() * len(array))];
			return randomValue;

		def formatInputs(frame, command, value):
			return f"{frame} {command} {value} \n"
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
		f.write(formatInputs(0, "gas", randomValFromArray(gas)))
		f.write(formatInputs(0, "brake", randomValFromArray(brakes)))
		f.write(formatInputs(0, "lean", randomValFromArray(leans)))
		f.write(formatInputs(100, "gas", randomValFromArray(gas)))
		f.write(formatInputs(100, "brake", randomValFromArray(brakes)))
		f.write(formatInputs(100, "lean", randomValFromArray(leans)))
		f.close()

		


