from factories.helix.normal_helix import NormalHelix
from factories.helix.redundant_helix import RedundantHelix


class HelixFactory:

	@staticmethod
	def get_helix(is_redundant: bool):
		"""
		Return a helix factory by providing his type
		"""

		if is_redundant:
			return RedundantHelix()

		return NormalHelix()
