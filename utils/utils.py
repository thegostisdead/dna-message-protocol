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