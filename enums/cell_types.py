from enum import Enum


class CellsTypes(Enum):
	"""Basic cells type that compose helix"""
	START = "start"
	LENGTH = "length"
	CHECKSUM = "checksum"
	DATA = "data"
	END = "end"
