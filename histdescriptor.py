#import the necessary packages
import numpy as np
import cv2
import sys

class HistDescriptor:
	def __init__(self, bins):
		# store the number of bins for the 3D histogram
		self.bins = bins

	def describe(self, image):
		# convert the image to the HSV color space and initialize
		# the features used to quantify the image
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []

		features = cv2.calcHist([image], [0,1,2], None, self.bins, [0, 180, 0, 256, 0, 256])
		features = cv2.normalize(features).flatten()

		# return the feature vector
		return features