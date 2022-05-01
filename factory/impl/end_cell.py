from factory.cell import Cell


class EndCell(Cell):

	def get_size(self) -> int:
		pass

	def get_left(self) -> dict:
		pass

	def get_right(self) -> dict:
		pass

	def get_info(self) -> dict:
		print("je suis EndCell")
