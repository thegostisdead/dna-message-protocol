# 1 -> lecture du message -> ✅
# 2 -> Conversion en sequence ascii ✅
# 3 -> Selection du mode (red/non red)
# 4 -> Initialisation Helix
# 5 -> Initialisation des premieres cells (init , end)
# 6 -> Découper notre sequence de code ascii en paquet de 4 (a voir )

import sys
import argparse


def parse_args():
	"""
	Parse input arguments
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--message', required=True,
	                    help='The message to encode', )
	parser.add_argument('-r', '--redundant',
	                    help='If the message need to be redundant',
	                    type=str, default=False)

	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit(1)

	args = parser.parse_args()
	return args


parsed_args = parse_args()
print(parsed_args)

from encoder.encoder import Encoder

ascii_sequence = Encoder.encode(parsed_args.message)

print(ascii_sequence)

if parsed_args.redundant:
	# ask for a redundant cell
	pass
else:
	# use normal cell
	pass