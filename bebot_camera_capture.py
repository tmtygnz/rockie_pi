import base64

import cv2 as cv


class CameraCapture:
	def __init__(self):
		self.capturer = cv.VideoCapture(0)

	def getImageBytes(self):
		ret, img = self.capturer.read()
		if ret:
			image_png, buf = cv.imencode(".jpg", img, [cv.IMWRITE_JPEG_QUALITY, 10])

			return buf.tobytes()
		else:
			return None
