import random

import serial


class SerialReader:
	def __init__(self):
		try:
			self.ser = serial.Serial(port="COM11", baudrate=9600, timeout=1)
		except:
			pass

	def getLine(self):
		return self.ser.readline().decode("utf-8").strip()

	def getLineFake(self):
		v = random.uniform(-0.1, 0.1)
		p = random.uniform(-0.1, 0.1)
		r = random.uniform(-0.1, 0.1)
		y = random.uniform(-0.1, 0.1)
		result = f"{v},{p},{r},{y}"
		return result
