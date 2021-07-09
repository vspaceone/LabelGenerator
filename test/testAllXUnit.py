
# Author:    Maximilian Noppel
# Date:      April 2021

import unittest
import xmlrunner

import context

from testLabelGenerator import *
from testHelper import *
from testCMDInterface import *
from testServer import *
from testFlask import *





class TestAll(unittest.TestCase):
	pass

if __name__ == '__main__':
	with open('../results.xml', 'wb') as output:
		unittest.main(
			testRunner=xmlrunner.XMLTestRunner(output=output),
			failfast=False, buffer=False, catchbreak=False)
		output.close()