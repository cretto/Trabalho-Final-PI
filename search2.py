# import the necessary packages
from texturedescriptor import TextureDescriptor
from searcher import Searcher
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--index", required = True,
#	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
#ap.add_argument("-r", "--result-path", required = True,
#	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
#cd = ColorDescriptor((8,12,3))

# load the query image and describe it
img = cv2.imread(args["query"])
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
img = magnitude_spectrum

#features = cd.describe(query)

# perform the search
#searcher = Searcher(args["index"])
#results = searcher.search(features, 10)

# dislpay the query
r = 800.0 / img.shape[1]
dim = (800, int(img.shape[0] * r))

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Query", resized)
cv2.waitKey(0)

# loop over the results
#for (score, resultID) in results:

	#load the result image and display it
#	result = cv2.imread(args["result_path"]+"/"+resultID)
	
#	r = 800.0 / result.shape[1]
#	dim = (800, int(result.shape[0] * r))

#	resized = cv2.resize(result, dim, interpolation = cv2.INTER_AREA)
#	cv2.imshow("Result", resized)
#	cv2.waitKey(0)
#	print result
