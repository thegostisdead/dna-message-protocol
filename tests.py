import unittest
from factories import CellFactory, Cell
from factories.cell import ChecksumCell, EndCell, StartCell, DataCell


class TestDNACore(unittest.TestCase):

	def test_factory(self):
		""" Test if the cell factories return the correct object"""

		cell_factory = CellFactory()

		cell01 = cell_factory.get_cell("start")
		cell02 = cell_factory.get_cell("data")
		cell03 = cell_factory.get_cell("checksum")
		cell04 = cell_factory.get_cell("end")

		message_start = "given object is not instance of StartCell."
		message_data = "given object is not instance of DataCell."
		message_check = "given object is not instance of ChecksumCell."
		message_end = "given object is not instance of EndCell."

		self.assertIsInstance(cell01, StartCell, message_start)
		self.assertIsInstance(cell02, DataCell, message_data)
		self.assertIsInstance(cell03, ChecksumCell, message_check)
		self.assertIsInstance(cell04, EndCell, message_end)

	def test_factory_negative(self):
		""" Test if the cell factories return the bad object"""

		cell_factory = CellFactory()
		cell01 = cell_factory.get_cell("start")
		self.assertEqual(not isinstance(cell01, StartCell), False)

	def test_factory_interface(self):
		""" Test if the cell factories return the bad object"""

		self.assertEqual(issubclass(ChecksumCell, Cell), True)
		self.assertEqual(issubclass(EndCell, Cell), True)
		self.assertEqual(issubclass(StartCell, Cell), True)
		self.assertEqual(issubclass(DataCell, Cell), True)

	def test_factory_generated_type(self):
		""" Test if the cell factories return the bad object"""

		cell_factory = CellFactory()
		cell01 = cell_factory.get_cell("start")
		cell02 = cell_factory.get_cell("data")
		cell03 = cell_factory.get_cell("checksum")
		cell04 = cell_factory.get_cell("end")

		self.assertEqual(isinstance(cell01, Cell), True)
		self.assertEqual(isinstance(cell02, Cell), True)
		self.assertEqual(isinstance(cell03, Cell), True)
		self.assertEqual(isinstance(cell04, Cell), True)


if __name__ == '__main__':
	unittest.main()
