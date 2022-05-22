import argparse
import sys

from rich import inspect

from encoder.encoder import Encoder


class Utils:
	@staticmethod
	def bind_left_right(cell, value):
		"""Bind data to left cell and his right complement"""
		cell.add_nucleotide_left(value)
		cell.add_nucleotide_right(Utils.invert_dna_sequence(value))

	@staticmethod
	def dump(object_to_dump):
		""" Display an object with rich"""
		inspect(object_to_dump, methods=True)

	@staticmethod
	def invert_dna_sequence(sequence):
		""" Get the complement of a given dna sequence"""
		complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
		seq_list = list(sequence)
		return [complement_dict[base] for base in seq_list]

	@staticmethod
	def parse_args():
		"""
		Parse input arguments
		"""
		parser = argparse.ArgumentParser()
		parser.add_argument('-m', '--message', required=True,
		                    help='The message to encode', )
		parser.add_argument('-o', '--output', required=True,
		                    help='The output filename of generated image', )
		parser.add_argument('-r', '--redundant', action="store_true",
		                    help='If the message need to be redundant',
		                    default=False)

		if len(sys.argv) == 1:
			parser.print_help()
			sys.exit(1)

		args = parser.parse_args()
		return args

	@staticmethod
	def attach_int_value(cell, value):
		""" Add an int value to the left and automatically bind the complement to the right """

		base_seq = Encoder.ascii_to_dna_base([value])
		encoded_char = Encoder.replace_with_char(base_seq)
		for char in encoded_char:
			cell.add_nucleotide_left(char)
			cell.add_nucleotide_right(Utils.invert_dna_sequence(char))
