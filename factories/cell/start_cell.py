from factories.cell.cell import Cell
from utils.utils import Utils


class StartCell(Cell):

	def __init__(self, value):
		super().__init__()

		Utils.attach_int_value(self, value)

	def get_size(self) -> int:
		pass
