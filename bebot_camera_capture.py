import base64

import cv2 as cv


class CameraCapture:
	def __init__(self):
		self.capturer = cv.VideoCapture(0)

	def getImageBytes(self):
		ret, img = self.capturer.read()
		if ret:
			image_png, buf = cv.imencode(".png", img)

			return buf.tobytes()
		else:
			return None
