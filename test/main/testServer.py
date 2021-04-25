# Author:    Maximilian Noppel
# Date:      April 2021


import unittest

from src.main.Server import *


class TestServer(unittest.TestCase):
	"""
	TestServer: Test class for the flask server
	"""


	def test_generateWrongLabelType(self):
		with self.assertRaises(Exception):
			generate("beef", "Text", fileformat="png")

	def test_generateWrongFormat(self):
		with self.assertRaises(Exception):
			generate("give_away", "Text", fileformat="jpg")

if __name__ == '__main__':
	unittest.main()
