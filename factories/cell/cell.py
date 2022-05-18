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

	def get_left(self) -> list:
		"""Get the left column with dict (index in the list -> nucleotide)."""
		return self.left_nucleotide

	def get_right(self) -> list:
		"""Get the right column with dict (index in the list -> nucleotide)."""
		return self.right_nucleotide

	def add_nucleotide_left(self, nucleotide):
		self.left_nucleotide.append(nucleotide)

	def add_nucleotide_right(self, nucleotide):
		self.right_nucleotide.append(nucleotide)

	def display_info(self):
		"""Show the cell info."""
		inspect(self, methods=True)

	def __repr__(self):
		return f"DataCell[ left={self.left_nucleotide} right={self.right_nucleotide}]"
