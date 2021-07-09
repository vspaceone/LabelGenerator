# Author:    Maximilian Noppel
# Date:      April 2021


import unittest

from src.main.Helper import *


class TestHelper(unittest.TestCase):
	"""
	TestHelper: Test class for Helper file
	"""


	def test_printVersions(self):
		"""
		Test if printVersions works without exception
		:return: void
		"""
		printVersions()

	def test_getVersion(self):
		"""
		Test if getVersion return a non-empty string
		:return: void
		"""
		s = getVersion()
		self.assertEqual( str, type(s) )
		self.assertTrue(len(s) > 0)





if __name__ == '__main__':
	unittest.main()
