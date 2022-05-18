from .helix import Helix
from ..cell import StartCell, EndCell, SizeCell, ChecksumCell, DataCell
from utils.utils import Utils
from encoder.encoder import Encoder

CELL_SIZE = 4


class NormalHelix(Helix):

	def __init__(self, ):
		from ..cell import StartCell, EndCell
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
		base_seq = Encoder.ascii_to_dna_base(ascii_sequence)
		print(f"base_seq={base_seq}")
		self.full_dna_sequence = Encoder.replace_with_char(base_seq)

		for encoded_char in self.full_dna_sequence:
			computed_cell = DataCell()

			computed_cell.add_nucleotide_left(encoded_char)

			computed_cell.add_nucleotide_right(
				Utils.invert_dna_sequence(encoded_char))

			self.set_data_cell(computed_cell)

# here generate the data cells
