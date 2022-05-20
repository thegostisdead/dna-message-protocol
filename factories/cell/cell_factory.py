from factories.cell import Cell, StartCell, ChecksumCell, EndCell, DataCell

REDUNDANT_HELIX = 200
NORMAL_HELIX = 151


class CellFactory:

	@staticmethod
	def get_cell(wanted_cell_type: str, redundant=False) -> Cell:
		"""Return a cell by providing his type (based on enum)"""

		cells_types = {
			"start": StartCell(REDUNDANT_HELIX if redundant else NORMAL_HELIX),
			"data": DataCell(),
			"checksum": ChecksumCell(None),
			"end": EndCell()
		}

		if wanted_cell_type in cells_types:
			return cells_types[wanted_cell_type]
		print(f"Unknown cell type provided : {wanted_cell_type}.")
