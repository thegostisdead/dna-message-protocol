from abc import ABC, abstractmethod
from rich import inspect
from ..cell import StartCell, EndCell, SizeCell, ChecksumCell, DataCell


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
	def get_checksum(self):
		"""Add end cell"""

	def set_end_cell(self, cell):
		assert (isinstance(cell, EndCell))
		self.end = cell

	def set_start_cell(self, cell):
		assert (isinstance(cell, StartCell))
		self.start = cell

	def set_size_cell(self, cell):
		assert (isinstance(cell, SizeCell))
		self.size = cell

	def set_checksum_cell(self, cell):
		assert (isinstance(cell, ChecksumCell))
		self.size = cell

	def set_data_cell(self, cell):
		assert (isinstance(cell, DataCell))
		self.data.append(cell)

	def get_helix(self):
		from factories.cell import SizeCell
		updated_size_cell = SizeCell()
		message_size = len(self.data)

		from utils.utils import Utils
		Utils.attach_int_value(updated_size_cell, message_size)
		self.set_size_cell(updated_size_cell)
		self.get_checksum()
		return self

	def display_info(self):
		"""Show the helix info."""
		inspect(self, methods=True)
