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
		Test if buildImage throws an error for some inputs
		:return: void
		"""
		lg = LabelGenerator()
		lg.buildImage("give_away", "Text", outputfile=None)


if __name__ == '__main__':
	unittest.main()
