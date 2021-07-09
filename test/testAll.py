
# Author:    Maximilian Noppel
# Date:      April 2021

import unittest
import os

import context

from testLabelGenerator import *
from testHelper import *
from testCMDInterface import *
from testServer import *
from testFlask import *


os.chdir("..")

class TestAll(unittest.TestCase):
	pass

if __name__ == '__main__':
	unittest.main()