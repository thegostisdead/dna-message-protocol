import unittest

from factories import CellFactory, Cell
from factories.cell import ChecksumCell, EndCell, StartCell, DataCell

from factories.helix.helix_factory import HelixFactory
from factories.helix.normal_helix import NormalHelix
from factories.helix.redundant_helix import RedundantHelix
from utils.utils import Utils


class TestDNACore(unittest.TestCase):

	def test_start_redundant_cell_content(self):
		"""Test left and right list"""

		cell01 = CellFactory.get_cell("start", redundant=True)

		self.assertEqual(cell01.get_left() == [['G', 'A', 'C', 'A']], True)
		self.assertEqual(cell01.get_right() == [['C', 'T', 'G', 'T']], True)

	def test_start_normal_cell_content(self):
		"""Test left and right list"""

		cell01 = CellFactory.get_cell("start", redundant=False)

		self.assertEqual(cell01.get_left() == [['C', 'T', 'T', 'G']], True)
		self.assertEqual(cell01.get_right() == [['G', 'A', 'A', 'C']], True)

	def test_end_cell_content(self):
		"""Test left and right list"""

		cell01 = CellFactory.get_cell("end")

		self.assertEqual(cell01.get_left() == [['C', 'A', 'G', 'A']], True)
		self.assertEqual(cell01.get_right() == [['G', 'T', 'C', 'T']], True)

	def test_cell_factory(self):
		""" Test if the cell factories return the correct object"""

		cell01 = CellFactory.get_cell("start")
		cell02 = CellFactory.get_cell("data")
		cell03 = CellFactory.get_cell("checksum")
		cell04 = CellFactory.get_cell("end")

		message_start = "given object is not instance of StartCell."
		message_data = "given object is not instance of DataCell."
		message_check = "given object is not instance of ChecksumCell."
		message_end = "given object is not instance of EndCell."

		self.assertIsInstance(cell01, StartCell, message_start)
		self.assertIsInstance(cell02, DataCell, message_data)
		self.assertIsInstance(cell03, ChecksumCell, message_check)
		self.assertIsInstance(cell04, EndCell, message_end)

	def test_cell_factory_negative(self):
		""" Test if the cell factories return the bad object"""

		cell01 = CellFactory.get_cell("start")
		self.assertEqual(not isinstance(cell01, StartCell), False)

	def test_cell_factory_interface(self):
		""" Test if the cell factories return the bad object"""

		self.assertEqual(issubclass(ChecksumCell, Cell), True)
		self.assertEqual(issubclass(EndCell, Cell), True)
		self.assertEqual(issubclass(StartCell, Cell), True)
		self.assertEqual(issubclass(DataCell, Cell), True)

	def test_cell_factory_generated_type(self):
		""" Test if the cell factories return the bad object"""

		cell01 = CellFactory.get_cell("start")
		cell02 = CellFactory.get_cell("data")
		cell03 = CellFactory.get_cell("checksum")
		cell04 = CellFactory.get_cell("end")

		self.assertEqual(isinstance(cell01, Cell), True)
		self.assertEqual(isinstance(cell02, Cell), True)
		self.assertEqual(isinstance(cell03, Cell), True)
		self.assertEqual(isinstance(cell04, Cell), True)

	def test_helix_factory_generated_type(self):
		helix1 = HelixFactory.get_helix(is_redundant=True)
		helix2 = HelixFactory.get_helix(is_redundant=False)

		self.assertEqual(isinstance(helix1, RedundantHelix), True)
		self.assertEqual(isinstance(helix2, NormalHelix), True)

	def test_helix_factory_generated_type_init_attributes(self):
		helix1 = HelixFactory.get_helix(is_redundant=True)
		helix2 = HelixFactory.get_helix(is_redundant=False)

		self.assertEqual(isinstance(helix1.start, StartCell), True)
		self.assertEqual(isinstance(helix1.end, EndCell), True)

		self.assertEqual(isinstance(helix2.start, StartCell), True)
		self.assertEqual(isinstance(helix2.end, EndCell), True)


if __name__ == '__main__':
	unittest.main()
