from factories.helix.normal_helix import NormalHelix
from factories.helix.redundant_helix import RedundantHelix


class HelixFactory:

	@staticmethod
	def get_helix(is_redundant: bool):
		"""
		Return a helix factory by providing his type
		"""

		return RedundantHelix() if is_redundant else NormalHelix()
