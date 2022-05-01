from factory.cell import Cell
from factory.impl import *


class CellFactory:

	def get_cell(self, wanted_cell_type: str) -> Cell:
		"""Return a cell by providing his type (based on enum)"""
		cells_types = {
			"start": StartCell(),
			"data": DataCell(),
			"checksum": ChecksumCell(),
			"end": EndCell(),
		}

		if wanted_cell_type in cells_types:
			return cells_types[wanted_cell_type]
		print(f"Unknown cell type provided : {wanted_cell_type}.")
