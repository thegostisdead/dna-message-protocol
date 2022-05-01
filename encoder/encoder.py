from dataclasses import dataclass


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
