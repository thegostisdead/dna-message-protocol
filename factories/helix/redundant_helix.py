from encoder.encoder import Encoder
from utils.utils import Utils
from .helix import Helix
from ..cell import StartCell, EndCell, SizeCell, ChecksumCell, DataCell

REDUNDANT_HELIX = 200


class RedundantHelix(Helix):

	def __init__(self):
		super().__init__()
		self.set_start_cell(StartCell(REDUNDANT_HELIX))
		self.set_end_cell(EndCell())

	def add_checksum(self):
		self.set_checksum_cell(ChecksumCell(len(self.data) + 2))

	def get_message(self) -> str:
		return "".join(chr(x) for x in self.message_ascii)

	def add_message(self, ascii_sequence):
		"""Split here the sequence"""

		self.message_ascii = ascii_sequence
		base_seq = Encoder.ascii_to_dna_base(ascii_sequence)
		self.full_dna_sequence = Encoder.replace_with_char(base_seq)

		for encoded_char in self.full_dna_sequence:
			computed_cell = DataCell()

			computed_cell.add_nucleotide_left(encoded_char)
			computed_cell.add_nucleotide_right(
				Utils.invert_dna_sequence(encoded_char))

			self.set_data_cell(computed_cell)
			self.set_data_cell(computed_cell)
