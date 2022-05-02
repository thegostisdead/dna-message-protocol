from factories.helix.helix import Helix
from factories.helix import *


class HelixFactory:

	def get_cell(self, is_redundant: bool) -> Helix:
		"""
		Return a helix factory by providing his type
		"""

		if is_redundant:
			return RedundantHelix()

		return NormalHelix()
