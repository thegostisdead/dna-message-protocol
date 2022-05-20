from rich import inspect
import sys
import argparse


class Utils:
	@staticmethod
	def bind_left_right(cell, value):
		cell.add_nucleotide_left(value)
		cell.add_nucleotide_right(Utils.invert_dna_sequence(value))

	@staticmethod
	def get_helix_range(data, block_size):
		k = dict()
		helix_number = 0

		while len(data) > 0:

			for i in range(0, block_size):

				try:
					fist_elem = data[0]
					del data[0]

				except IndexError as e:
					fist_elem = None

				if helix_number in k:
					k[helix_number].append(fist_elem)
				else:
					k[helix_number] = []
					k[helix_number].append(fist_elem)

			helix_number += 1

		return k

	@staticmethod
	def dump(object_to_dump):
		inspect(object_to_dump, methods=True)

	@staticmethod
	def invert_dna_sequence(sequence):

		def complement(seq):
			"""Returns a complement DNA sequence"""
			complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
			seq_list = list(seq)
			seq_list = [complement_dict[base] for base in seq_list]

			return seq_list

		complement_seq = complement(sequence)
		return complement_seq

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

		from encoder.encoder import Encoder

		base_seq = Encoder.ascii_to_dna_base([value])
		encoded_char = Encoder.replace_with_char(base_seq)
		for char in encoded_char:
			cell.add_nucleotide_left(char)
			cell.add_nucleotide_right(Utils.invert_dna_sequence(char))
