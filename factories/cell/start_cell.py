from factories.cell.cell import Cell
from utils.utils import Utils

REDUNDANT_HELIX = 200  # 3020 base 4 => CAGA
NORMAL_HELIX = 151  # 2113 base 4 => GTTC


class StartCell(Cell):

	def __init__(self, is_redundant):
		super().__init__()

		Utils.attach_int_value(self,REDUNDANT_HELIX if is_redundant else NORMAL_HELIX)
