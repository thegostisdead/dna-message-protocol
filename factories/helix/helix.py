from abc import ABC, abstractmethod


class Helix(ABC):
	"""Basic representation of a helix."""

	def __init__(self):
		self.start = None
		self.s = None
		self.data = None
		self.end = None

	@abstractmethod
	def get_message(self) -> str:
		"""Return the message"""
