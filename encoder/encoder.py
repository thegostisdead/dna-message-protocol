from dataclasses import dataclass

from utils.utils import Utils


@dataclass
class Encoder:

	@staticmethod
	def get_ascii(char):
		return ord(char)

	@staticmethod
	def encode(message):
		ascii_message_sequence = []

		for char in message:
			ascii_message_sequence.append(Encoder.get_ascii(char))

		return ascii_message_sequence

	@staticmethod
	def ascii_to_dna_base(ascii_message_sequence):
		def numberToBase(char):
			if char == 0:
				return [0]
			digits = []
			while char:
				digits.append(int(char % 4))
				char //= 4
			return digits[::-1]

		return [numberToBase(x) for x in ascii_message_sequence]

	@staticmethod
	def replace_with_char(dna_base_sequence):

		print(dna_base_sequence)
		mapping = {
			0: "A",
			1: "T",
			2: "C",
			3: "G"
		}
		new_sec = []

		for char_bit in dna_base_sequence:
			tmp = []
			for bit in char_bit:
				tmp.append(mapping[bit])
			new_sec.append(tmp)

		return new_sec
