from .helix import Helix


class NormalHelix(Helix):

	def add_start_cell(self, start):
		self.start = start

	def add_size_cell(self, cell):
		self.size = cell

	def add_checksum_cell(self, cell):
		self.checksum = cell

	def add_data_cell(self, cell):
		self.data.append(cell)

	def add_end_cell(self, end):
		self.end = end

	def get_message(self) -> str:
		pass
