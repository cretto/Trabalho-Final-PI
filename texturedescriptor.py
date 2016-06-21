# import the necessary packages
import numpy as np
import cv2

class TextureDescriptor:
	def __init__(self, bins):
		# store the number of bins for the 3D histogram
		self.bins = bins

	def describe(self, image):
		# convert the image to the HSV color space and initialize
		# the features used to quantify the image
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []

		# grab the dimensions and compute the center of the image
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))

		# divide the image into four rectangles/segments (top-left,
		# top-right, bottom-right, bottom-left)
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),
			(0, cX, cY, h)]

		# construct an elliptical mask representing the center of the
		# image
		(axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
		ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)

		# loop over the segments
		for (startX, endX, startY, endY) in segments:
			# construct a mask for each corner of the image, subtracting
			# the elliptical center from it
			cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
			cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
			cornerMask = cv2.subtract(cornerMask, ellipMask)

			# extract a color histogram from the image, then update the
			# feature vector
			cv2.imshow(image)
			desc = self.fourier_tranform(image)
			features.extend(desc)

		# extract a color histogram from the elliptical region and
		# update the feature vector
		desc = self.fourier_tranform(image)
		features.extend(desc)

		# return the feature vector
		return features

	def fourier_tranform(self, image, mask):
		# extract a 3D color histogram from the masked region of the image, using the supplied number of bins
		# per channel; then nomalize the histogram
		#hist = cv2.calcHist([image], [0,1,2], mask, self.bins, [0, 180, 0, 256, 0, 256])
		#hist = cv2.normalize(hist).flatten()

		hist = np.fft.fft2(image)
		fshift = np.fft.fftshift(f)
		magnitude_spectrum = 20*np.log(np.abs(fshift))

		# return the histogram
		#return hist
		return magnitude_spectrum