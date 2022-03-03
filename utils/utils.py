# import the necessary packages
import imutils
import time
import cv2
import deepvision as dv
from deepvision.object_detection import draw_bbox

		
def sliding_window(image, StepSizeX, StepSizeY, windowSize, finalStep):
	global i
	i = 0
	# slide a window across the image
	for y in range(0, image.shape[0], StepSizeY):
		for x in range(0, image.shape[1], StepSizeX):
			# yield the current window
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])
			i = i + 1
			print(finalStep)
			print(i)
			if i == finalStep:
				break

def SlicedDetection(image, model="yolov4"):
	StepYKalan = int(image.shape[0]%256)
	StepYKat = int(image.shape[0]/256)
	StepEksi = int(256 - StepYKalan)
	Step = int(StepEksi/(StepYKat))
	StepSizeY = int(256-Step)
	print(StepSizeY)

	StepXKalan = int(image.shape[1]%256)
	StepXKat = int(image.shape[1]/256)
	StepEksi = int(256 - StepXKalan)
	Step = int(StepEksi/(StepXKat))
	StepSizeX = int(256-Step)
	print(StepSizeX)

	(winW, winH) = (256, 256)
	finalStep = (StepYKat + 2)*(StepXKat + 1)
	for (x, y, window) in sliding_window(image, StepSizeX=StepSizeX, StepSizeY=StepSizeY, windowSize=(winW, winH), finalStep=finalStep):
		# if the window does not meet our desired window size, ignore it

		clone = image.copy()
		bbox, label, conf = dv.detect_common_objects(window, model=model)

		newlist = []
		list1 = bbox

		for l in list1:
			n1 = l[0]+x
			n2 = l[1]+y
			n3 = l[2]+x
			n4 = l[3]+y
			n5 = [n1,n2,n3,n4]
			newlist.append(n5)

		# draw bounding box over detected objects
		#cv2.rectangle(image, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
		out = draw_bbox(image, newlist, label, conf)		
