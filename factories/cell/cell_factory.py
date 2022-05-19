from factories.cell import Cell, StartCell, ChecksumCell, EndCell, DataCell


class CellFactory:

	@staticmethod
	def get_cell(wanted_cell_type: str, redundant=False) -> Cell:
		"""Return a cell by providing his type (based on enum)"""

		cells_types = {
			"start": StartCell(200 if redundant else 151),
			# TODO replace magic values
			"data": DataCell(),
			"checksum": ChecksumCell(None),
			"end": EndCell()
		}

		if wanted_cell_type in cells_types:
			return cells_types[wanted_cell_type]
		print(f"Unknown cell type provided : {wanted_cell_type}.")
