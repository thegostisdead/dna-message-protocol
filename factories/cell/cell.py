from abc import ABC, abstractmethod

from rich import inspect

CELL_SIZE = 4  # number of lines in a single cells


class Cell(ABC):
	"""Basic representation of cell."""

	def __init__(self):
		self.size = CELL_SIZE
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

	def display_info(self):
		"""Show the cell info."""
		inspect(self, methods=True)
