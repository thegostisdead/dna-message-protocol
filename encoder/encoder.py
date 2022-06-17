class Encoder:

	@staticmethod
	def get_ascii(char):
		return ord(char)

	@staticmethod
	def encode(message):
		return [Encoder.get_ascii(char) for char in message]

	@staticmethod
	def number_to_base(char):
		if char == 0:
			return [0]
		digits = []
		while char:
			digits.append(int(char % 4))
			char //= 4
		return digits[::-1]

	@staticmethod
	def ascii_to_dna_base(ascii_message_sequence):
		return [Encoder.number_to_base(x) for x in ascii_message_sequence]

	@staticmethod
	def replace_with_char(dna_base_sequence):

		mapping = {
			0: "A",
			1: "T",
			2: "G",
			3: "C"
		}
		new_sec = []

		for char_bit in dna_base_sequence:
			tmp = [mapping[bit] for bit in char_bit]
			new_sec.append(tmp)

		return new_sec
