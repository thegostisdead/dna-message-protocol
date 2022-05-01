from encoder import Encoder
from cell import Cell
from utils import Utils


class Helix:

	def __init__(self, is_redundant=False, size_of_cells=8):
		self.is_redundant = is_redundant
		self.text_data = None
		self.size_of_cells = size_of_cells

		# cells
		self.first_cell = None
		self.len_cell = None
		self.size_cell = None
		self.checksum_cell = None
		self.cells = []  # data here
		self.end_cell = None

	def init_cells(self):
		self.first_cell = Cell().add_init_flag(self.is_redundant)

	def add_checksum(self):
		self.checksum_cell = Utils.compute_checksum(self.get_ascii_message())

	def add_text_message(self, text):
		self.text_data = text

	def get_text_message(self):
		return self.text_data

	def get_cells(self):
		return self.cells

	def get_ascii_message(self):
		return Encoder.encode(self.text_data)

	def __repr__(self):
		return f"==Helix==\n" \
		       f"is_redundant={self.is_redundant} \n" \
		       f"text_data={self.get_text_message()} \n" \
		       f"ascii={self.get_ascii_message()} \n" \
		       f"size_cell={self.size_of_cells} \n" \
		       f"current_number_cell={len(self.get_cells())} \n" \
		       f"==---==\n"
