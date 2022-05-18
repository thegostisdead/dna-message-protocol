from .helix import Helix
from ..cell import StartCell, EndCell, SizeCell, ChecksumCell, DataCell


class RedundantHelix(Helix):

	def __init__(self, ):
		super().__init__()
		self.set_start_cell(StartCell())
		self.set_end_cell(EndCell())

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

	def set_end_cell(self, cell):
		assert (isinstance(cell, EndCell))
		self.end = cell

	def get_message(self) -> str:
		pass

	def add_message(self, ascii_sequence):
		"""Split here the sequence"""
		self.message_ascii = ascii_sequence
