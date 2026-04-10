import json
from dataclasses import dataclass
from typing import Union

import msgpack
import pynng


@dataclass
class Message:
	message: str
	content: Union[str, bytes]

	def to_dict(self):
		return {"message": self.message, "content": self.content}


class GuestNet:
	def __init__(self):
		self.socket = pynng.Pair1(dial="tcp://192.168.100.53:5555")

	def send_data(self, to: str, content: Union[str, bytes]):
		tbs = msgpack.packb(Message(to, content).to_dict())
		self.socket.send(tbs)

	def send_data_raw(self, data):
		self.socket.send(str(data).encode("utf-8"))
