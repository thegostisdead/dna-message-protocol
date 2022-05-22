from abc import ABC

from rich import inspect

CELL_SIZE = 4  # number of lines in a single cells


class Cell(ABC):
	"""Basic representation of cell."""

	def __init__(self):
		self.size = CELL_SIZE
		self.left_nucleotide = []
		self.right_nucleotide = []

	def get_left(self) -> list:
		"""Return the left side"""
		return self.left_nucleotide

	def get_right(self) -> list:
		"""Return the right side (complement of the left side)"""
		return self.right_nucleotide

	def add_nucleotide_left(self, nucleotide):
		"""Append left a new nucleotide"""
		self.left_nucleotide.append(nucleotide)

	def add_nucleotide_right(self, nucleotide):
		"""Append right a new nucleotide"""
		self.right_nucleotide.append(nucleotide)

	def display_info(self):
		"""Display cell with rich"""
		inspect(self, methods=True)

	def __repr__(self):
		return f"DataCell[ left={self.left_nucleotide} right={self.right_nucleotide}]"
