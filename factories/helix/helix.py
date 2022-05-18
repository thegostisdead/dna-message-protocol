from abc import ABC, abstractmethod
from rich import inspect


class Helix(ABC):
	"""Basic representation of a helix."""

	def __init__(self):
		self.start = None
		self.size = None
		self.checksum = None
		self.data = []  # list of cells
		self.end = None
		self.message_ascii = []
		self.full_dna_sequence = []

	@abstractmethod
	def get_message(self) -> str:
		"""Return the message"""

	@abstractmethod
	def add_message(self, ascii_sequence):
		"""Split here the sequence"""

	@abstractmethod
	def set_start_cell(self, cell):
		"""Add the start cell"""

	@abstractmethod
	def set_size_cell(self, cell):
		"""Add the size cell"""

	@abstractmethod
	def set_checksum_cell(self, cell):
		"""Add the checksum cell"""

	@abstractmethod
	def set_data_cell(self, cell):
		"""Add a data cell"""

	@abstractmethod
	def set_end_cell(self, cell):
		"""Add end cell"""

	def display_info(self):
		"""Show the helix info."""
		inspect(self, methods=True)
