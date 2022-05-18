from factories.cell.cell import Cell


class DataCell(Cell):

	def get_size(self) -> int:
		return len(self.left_nucleotide)

	def get_left(self):
		return self.left_nucleotide

	def get_right(self):
		return self.right_nucleotide
