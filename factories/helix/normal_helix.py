from .helix import Helix
from ..cell import StartCell, EndCell, SizeCell, ChecksumCell, DataCell
from utils.utils import Utils
from encoder.encoder import Encoder

CELL_SIZE = 4
NORMAL_HELIX_VALUE = 151


class NormalHelix(Helix):

	def __init__(self, ):
		from ..cell import StartCell, EndCell
		super().__init__()

		self.set_start_cell(StartCell(NORMAL_HELIX_VALUE))
		self.set_end_cell(EndCell())

	def set_start_cell(self, cell):
		assert (isinstance(cell, StartCell))
		self.start = cell

	def set_size_cell(self, cell):
		assert (isinstance(cell, SizeCell))
		self.size = cell

	def set_checksum_cell(self, cell):
		assert (isinstance(cell, ChecksumCell))
		self.checksum = cell

	def set_data_cell(self, cell):
		assert (isinstance(cell, DataCell))
		self.data.append(cell)

	def set_end_cell(self, cell):
		assert (isinstance(cell, EndCell))
		self.end = cell

	def get_message(self) -> str:
		return "".join(chr(x) for x in self.message_ascii)

	def get_checksum(self):
		self.set_checksum_cell(ChecksumCell(len(self.data) + 1))

	def add_message(self, ascii_sequence):
		"""Split here the sequence"""
		self.message_ascii = ascii_sequence
		base_seq = Encoder.ascii_to_dna_base(ascii_sequence)
		self.full_dna_sequence = Encoder.replace_with_char(base_seq)

		for encoded_char in self.full_dna_sequence:
			computed_cell = DataCell()
			Utils.bind_left_right(computed_cell, encoded_char)
			self.set_data_cell(computed_cell)
