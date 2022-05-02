"""
from helix import Helix
helix = Helix()
helix.add_text_message("bonjour les amis")

"""
from factories import *


def main():
	factory = CellFactory()

	cell01 = factory.get_cell("start")
	cell01.display_info()

	cell02 = factory.get_cell("end")
	cell02.display_info()


if __name__ == "__main__":
	main()
