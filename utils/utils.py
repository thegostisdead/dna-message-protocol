from rich import inspect
import sys
import argparse


class Utils:

	@staticmethod
	def compute_checksum(message) -> int:
		# message is ascii int array

		return sum(message)

	@staticmethod
	def find_checksum(message, k):

		# Dividing sent message in packets of k bits.
		c1 = message[0:k]
		c2 = message[k:2 * k]
		c3 = message[2 * k:3 * k]
		c4 = message[3 * k:4 * k]

		# Calculating the binary sum of packets
		packet_sum = bin(int(c1, 2) + int(c2, 2) + int(c3, 2) + int(c4, 2))[2:]

		# Adding the overflow bits
		if len(packet_sum) > k:
			x = len(packet_sum) - k
			packet_sum = bin(int(packet_sum[0:x], 2) + int(packet_sum[x:], 2))[
			             2:]
		if len(packet_sum) < k:
			packet_sum = '0' * (k - len(packet_sum)) + packet_sum

		# Calculating the complement of sum
		checksum = ''
		for i in packet_sum:
			if i == '1':
				checksum += '0'
			else:
				checksum += '1'
		return checksum

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
		parser.add_argument('-r', '--redundant', action="store_true",
		                    help='If the message need to be redundant',
		                    default=False)

		if len(sys.argv) == 1:
			parser.print_help()
			sys.exit(1)

		args = parser.parse_args()
		return args
