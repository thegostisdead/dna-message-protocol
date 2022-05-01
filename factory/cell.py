from abc import ABC, abstractmethod


class Cell(ABC):
	"""Basic representation of cell."""

	def __init__(self, size=8):
		self.size = size
		self.left_nucleotide = []
		self.right_nucleotide = []

	@abstractmethod
	def get_size(self) -> int:
		"""Get the number of nucleotide stored vertically."""

	@abstractmethod
	def get_left(self) -> dict:
		"""Get the left column with dict (index in the list -> nucleotide)."""

	@abstractmethod
	def get_right(self) -> dict:
		"""Get the right column with dict (index in the list -> nucleotide)."""

	@abstractmethod
	def get_info(self) -> dict:
		"""Get the cell info."""
