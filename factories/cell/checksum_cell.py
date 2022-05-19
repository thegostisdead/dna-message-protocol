from factories.cell.cell import Cell
from utils.utils import Utils


class ChecksumCell(Cell):

	def __init__(self, value):
		super().__init__()
		if value is not None:
			Utils.attach_int_value(self, value)

	def get_size(self) -> int:
		pass
