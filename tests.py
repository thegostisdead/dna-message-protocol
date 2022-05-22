import unittest

from encoder.encoder import Encoder
from factories import CellFactory, Cell
from factories.cell import ChecksumCell, EndCell, StartCell, DataCell

from factories.helix.helix_factory import HelixFactory
from factories.helix.normal_helix import NormalHelix
from factories.helix.redundant_helix import RedundantHelix


class TestDNACore(unittest.TestCase):

	def test_start_redundant_cell_content(self):

		cell01 = CellFactory.get_cell("start", redundant=True)

		self.assertEqual(cell01.get_left(), [['C', 'A', 'G', 'A']])
		self.assertEqual(cell01.get_right(), [['G', 'T', 'C', 'T']])

	def test_start_normal_cell_content(self):

		cell01 = CellFactory.get_cell("start", redundant=False)
		# GTTC - CAAG
		self.assertEqual(cell01.get_left(), [['G', 'T', 'T', 'C']])
		self.assertEqual(cell01.get_right(),[['C', 'A', 'A', 'G']])

	def test_end_cell_content(self):

		cell01 = CellFactory.get_cell("end")
		# GACA -> CTGT
		self.assertEqual(cell01.get_left(), [['G', 'A', 'C', 'A']])
		self.assertEqual(cell01.get_right(), [['C', 'T', 'G', 'T']])

	def test_cell_factory(self):

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

		cell01 = CellFactory.get_cell("start")
		self.assertEqual(not isinstance(cell01, StartCell), False)

	def test_cell_factory_interface(self):
		self.assertEqual(issubclass(ChecksumCell, Cell), True)
		self.assertEqual(issubclass(EndCell, Cell), True)
		self.assertEqual(issubclass(StartCell, Cell), True)
		self.assertEqual(issubclass(DataCell, Cell), True)

	def test_cell_factory_generated_type(self):

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

	def test_helix_normal_helix(self):
		helix = HelixFactory.get_helix(is_redundant=False)
		helix.add_message(Encoder.encode("dorian"))
		self.assertEqual(helix.get_message(), "dorian")
		computed_helix = helix.get_helix()
		self.assertEqual(computed_helix.checksum.get_left(), [['T', 'C']])
		self.assertEqual(computed_helix.checksum.get_right(), [['A', 'G']])
		self.assertEqual(computed_helix.data[0].get_left(),
		                 [['T', 'G', 'T', 'A']])
		self.assertEqual(computed_helix.data[1].get_left(),
		                 [['T', 'G', 'C', 'C']])
		self.assertEqual(computed_helix.data[2].get_left(),
		                 [['T', 'C', 'A', 'G']])
		self.assertEqual(computed_helix.data[3].get_left(),
		                 [['T', 'G', 'G', 'T']])
		self.assertEqual(computed_helix.data[4].get_left(),
		                 [['T', 'G', 'A', 'T']])
		self.assertEqual(computed_helix.data[5].get_left(),
		                 [['T', 'G', 'C', 'G']])

	def test_helix_redundant_helix(self):
		helix = HelixFactory.get_helix(is_redundant=True)
		helix.add_message(Encoder.encode("dorian"))
		self.assertEqual(helix.get_message(), "dorian")
		computed_helix = helix.get_helix()
		self.assertEqual(computed_helix.checksum.get_left(), [['C', 'G']])
		self.assertEqual(computed_helix.checksum.get_right(), [['G', 'C']])
		self.assertEqual(computed_helix.data[0].get_left(),
		                 [['T', 'G', 'T', 'A']])
		self.assertEqual(computed_helix.data[1].get_left(),
		                 [['T', 'G', 'T', 'A']])
		self.assertEqual(computed_helix.data[2].get_left(),
		                 [['T', 'G', 'C', 'C']])
		self.assertEqual(computed_helix.data[3].get_left(),
		                 [['T', 'G', 'C', 'C']])
		self.assertEqual(computed_helix.data[2].get_left(),
		                 [['T', 'G', 'C', 'C']])
		self.assertEqual(computed_helix.data[2].get_left(),
		                 [['T', 'G', 'C', 'C']])
		self.assertEqual(computed_helix.data[3].get_left(),
		                 [['T', 'G', 'C', 'C']])
		self.assertEqual(computed_helix.data[4].get_left(),
		                 [['T', 'C', 'A', 'G']])
		self.assertEqual(computed_helix.data[5].get_left(),
		                 [['T', 'C', 'A', 'G']])


if __name__ == '__main__':
	unittest.main()
