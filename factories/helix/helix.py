from abc import ABC, abstractmethod


class Helix(ABC):
	"""Basic representation of a helix."""

	def __init__(self):
		self.start = None
		self.size = None
		self.checksum = None
		self.data = []  # list of cells
		self.end = None

	@abstractmethod
	def get_message(self) -> str:
		"""Return the message"""

	@abstractmethod
	def add_start_cell(self, cell):
		"""Add the start cell"""

	@abstractmethod
	def add_size_cell(self, cell):
		"""Add the size cell"""

	@abstractmethod
	def add_checksum_cell(self, cell):
		"""Add the checksum cell"""

	@abstractmethod
	def add_data_cell(self, cell):
		"""Add a data cell"""

	@abstractmethod
	def add_end_cell(self, cell):
		"""Add end cell"""
