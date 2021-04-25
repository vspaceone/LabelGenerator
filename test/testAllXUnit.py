
# Author:    Maximilian Noppel
# Date:      April 2021

import unittest
import xmlrunner

from test.main.testLabelGenerator import *
from test.main.testHelper import *
from test.main.testCMDInterface import *
from test.main.testServer import *


class TestAll(unittest.TestCase):
	pass

if __name__ == '__main__':
	with open('results.xml', 'wb') as output:
		unittest.main(
			testRunner=xmlrunner.XMLTestRunner(output=output),
			failfast=False, buffer=False, catchbreak=False)
		output.close()