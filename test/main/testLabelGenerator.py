# Author:    Maximilian Noppel
# Date:      April 2021


import unittest

from src.main.LabelGenerator import LabelGenerator


class TestLabelGenerator(unittest.TestCase):
	"""
	TestLabelGenerator: Test class for LabelGenerator
	"""


	def test_buildImageNormal(self):
		"""
		Test if buildImage works when called normally
		:return: void
		"""
		lg = LabelGenerator()
		lg.buildImage("give_away", "Text", outputfile=None)

	def test_buildImageGiveAwayWithEmptyText(self):
		"""
		Test if buildImage works normally for GiveAway with empty text
		:return: void
		"""
		lg = LabelGenerator()
		lg.buildImage("give_away", "", outputfile=None)

	def test_buildImageWrongLabel(self):
		"""
		Test if buildImage throws an error for unknown label type
		:return: void
		"""
		lg = LabelGenerator()
		with self.assertRaises(Exception):
			lg.buildImage("beef", "Text", outputfile=None)

	def test_buildImageUndocumentedWithEmptyText(self):
		"""
		Test if buildImage throws an error for labels different to
		GiveAway and an empty text.
		:return: void
		"""
		lg = LabelGenerator()
		with self.assertRaises(Exception):
			lg.buildImage("undocumented", "", outputfile=None)


if __name__ == '__main__':
	unittest.main()
