# Author:    Maximilian Noppel
# Date:      April 2021


import unittest
import argparse
import sys

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
		sys.argv = ["prog", "-l", "give_away", "-t","Test"]
		commandlineInterface()

	def test_commandlineInterfaceDifferentOrder(self):
		"""
		Test if commandlineInterface works without exception
		:return: void
		"""
		sys.argv = ["prog", "-t","Test", "-l", "give_away"]
		commandlineInterface()

	def test_commandlineInterfaceWithoutLabel(self):
		"""
		Test if commandlineInterface throws exception if no label is provided
		:return: void
		"""
		sys.argv = ["prog", "-t","Test"]
		with self.assertRaises(Exception):
			commandlineInterface()

	def test_commandlineInterfaceWithoutText(self):
		"""
		Test if commandlineInterface works if no text is provided
		:return: void
		"""
		sys.argv = ["prog", "-l", "public"]
		commandlineInterface()

	def test_commandlineInterfaceWithoutUnknownLabel(self):
		"""
		Test if commandlineInterface throws exception if label is unknown
		:return: void
		"""
		sys.argv = ["prog", "-l", "beef"]
		with self.assertRaises(Exception):
			commandlineInterface()







if __name__ == '__main__':
	unittest.main()
