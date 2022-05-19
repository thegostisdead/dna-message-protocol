from encoder.encoder import Encoder
from factories.cell.cell import Cell
from utils.utils import Utils

END_VALUE = 140


class EndCell(Cell):

	def __init__(self):
		super().__init__()

		Utils.attach_int_value(self, END_VALUE)

	def get_size(self) -> int:
		pass
