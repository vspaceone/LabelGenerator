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
	def test_commandlineInterface_Version(self):
		"""
		Test if commandlineInterface works without exception
		:return: void
		"""
		sys.argv = ["prog", "-v"]
		commandlineInterface()

	def test_commandlineInterface_Help(self):
		"""
		Test if commandlineInterface works without exception
		:return: void
		"""
		sys.argv = ["prog", "-h"]
		commandlineInterface()

	def test_commandlineInterface_Normal(self):
		"""
		Test if commandlineInterface works without exception
		:return: void
		"""
		sys.argv = ["prog", "-l", "give_away", "-t","Test"]
		commandlineInterface()

	def test_commandlineInterface_NormalWithOutput(self):
		"""
		Test if commandlineInterface works without exception
		:return: void
		"""
		sys.argv = ["prog", "-l", "give_away", "-t","Test", "-o", "delme.png"]
		commandlineInterface()

	def test_commandlineInterface_DifferentOrder(self):
		"""
		Test if commandlineInterface works without exception
		:return: void
		"""
		sys.argv = ["prog", "-t","Test", "-l", "give_away"]
		commandlineInterface()

	def test_commandlineInterface_WithoutLabel(self):
		"""
		Test if commandlineInterface throws exception if no label is provided
		:return: void
		"""
		sys.argv = ["prog", "-t","Test"]
		with self.assertRaises(Exception):
			commandlineInterface()

	def test_commandlineInterface_WithoutText(self):
		"""
		Test if commandlineInterface works if no text is provided
		:return: void
		"""
		sys.argv = ["prog", "-l", "public"]
		commandlineInterface()

	def test_commandlineInterface_WithoutUnknownLabel(self):
		"""
		Test if commandlineInterface throws exception if label is unknown
		:return: void
		"""
		sys.argv = ["prog", "-l", "beef"]
		with self.assertRaises(Exception):
			commandlineInterface()







if __name__ == '__main__':
	unittest.main()
