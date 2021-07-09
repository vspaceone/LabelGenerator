# Author:    Maximilian Noppel
# Date:      April 2021


import unittest

from Server import *


class TestServer(unittest.TestCase):
	"""
	TestServer: Test class for the flask server
	"""


	def test_generate_WrongLabelType(self):
		with self.assertRaises(Exception):
			generate("beef", "Text", fileformat="png")

	def test_generate_WrongFormat(self):
		with self.assertRaises(Exception):
			generate("give_away", "Text", fileformat="jpg")

	def test_startServer_PortStr(self):
		sys.argv = ["prog", "-p", "Test"]
		with self.assertRaises(Exception):
			startServer()

	def test_startServer_PortFloat(self):
		sys.argv = ["prog", "-p", "4.2"]
		with self.assertRaises(Exception):
			startServer()

	def test_startServer_IpFloat(self):
		sys.argv = ["prog", "-i", "4.2"]
		with self.assertRaises(Exception):
			startServer()

	def test_startServer_IpStr(self):
		sys.argv = ["prog", "-i", "Test"]
		with self.assertRaises(Exception):
			startServer()

	#def test_startServer_IpLocalhost(self):
	#	sys.argv = ["prog", "-i", "localhost"]
	#	with self.assertRaises(Exception):
	#		startServer()

	def test_startServer_DebugStr(self):
		sys.argv = ["prog", "-d", "localhost"]
		with self.assertRaises(Exception):
			startServer()

if __name__ == '__main__':
	unittest.main()
