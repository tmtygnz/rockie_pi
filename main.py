import asyncio
import json
import time

import pynng

from bebot_camera_capture import CameraCapture
from bebot_net import GuestNet, Message
from bebot_serial import SerialReader

network = GuestNet()
arial = SerialReader()
cam_cap = CameraCapture()


async def main():
	while True:
		line = arial.getLineFake()
		v, p, r, y = parse_line(line)

		await asyncio.gather(send_telemetry(v, p, r, y), send_camera())
		await asyncio.sleep(0)


async def send_telemetry(v, p, r, y):
	tasks = [
		asyncio.to_thread(network.send_data, "estivel", str(v)),
		asyncio.to_thread(network.send_data, "pitch", str(p)),
		asyncio.to_thread(network.send_data, "roll", str(r)),
		asyncio.to_thread(network.send_data, "yaw", str(y)),
	]

	await asyncio.gather(*tasks)


async def send_camera():
	image_buffer = cam_cap.getImageBytes()
	if image_buffer:
		await asyncio.to_thread(network.send_data, "cam", image_buffer)


def parse_line(line):
	try:
		v, p, r, y = map(float, line.split(","))
		print(v, p, r, y)
		return v, p, r, y
	except:
		return 0, 0, 0, 0


if __name__ == "__main__":
	asyncio.run(main())
