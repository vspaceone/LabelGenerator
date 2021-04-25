# Author:    Maximilian Noppel
# Date:      April 2021


import unittest

from src.main.CMDInterface import *


class TestCMDInterface(unittest.TestCase):
	"""
	TestHelper: Test class for Helper file
	"""


	def test_commandlineInterface(self):
		"""
		Test if commandlineInterface works without exception
		:return: void
		"""
		commandlineInterface()







if __name__ == '__main__':
	unittest.main()
