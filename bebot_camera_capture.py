import base64

import cv2 as cv


class CameraCapture:
	def __init__(self):
		self.capturer = cv.VideoCapture(0, cv.CAP_V4L2)
		self.capturer.set(cv.CAP_PROP_BUFFERSIZE, 1)
		self.capturer.set(cv.CAP_PROP_FPS, 25)
		self.capturer.set(cv.CAP_PROP_FRAME_WIDTH, 320)
		self.capturer.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
		self.capturer.set(cv.CAP_PROP_FOURCC, 1196444237)

	def getImageBytes(self):
		ret, img = self.capturer.read()
		if ret:
			image_png, buf = cv.imencode(".jpg", img, [cv.IMWRITE_JPEG_QUALITY, 70])

			return buf.tobytes()
		else:
			return None
