from abc import ABC, abstractmethod
from rich import inspect
from ..cell import StartCell, EndCell, SizeCell, ChecksumCell, DataCell
from utils.utils import Utils


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
	def add_checksum(self):
		"""Compute the checksum and bind it to Helix"""

	def set_end_cell(self, cell):
		"""Add the end cell to Helix"""
		assert (isinstance(cell, EndCell))
		self.end = cell

	def set_start_cell(self, cell):
		"""Add the start cell to Helix"""
		assert (isinstance(cell, StartCell))
		self.start = cell

	def set_size_cell(self, cell):
		"""Add the size cell to Helix"""
		assert (isinstance(cell, SizeCell))
		self.size = cell

	def set_checksum_cell(self, cell):
		"""Add the checksum cell to Helix"""
		assert (isinstance(cell, ChecksumCell))
		self.checksum = cell

	def set_data_cell(self, cell):
		"""Add the data cell to Helix"""
		assert (isinstance(cell, DataCell))
		self.data.append(cell)

	def get_helix(self):
		"""Return the helix with all cells computed and attached"""
		updated_size_cell = SizeCell()
		message_size = len(self.data)

		Utils.attach_int_value(updated_size_cell, message_size)
		self.set_size_cell(updated_size_cell)
		self.add_checksum()
		return self

	def display_info(self):
		"""Show the helix info by using rich."""
		inspect(self, methods=True)
