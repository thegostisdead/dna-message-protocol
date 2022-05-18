from factories.cell.cell import Cell


class DataCell(Cell):

	def get_size(self) -> int:
		return len(self.left_nucleotide)

	def __repr__(self) -> str:
		return super().__repr__()
