# -*- coding: utf-8 -*-
from rt.zps.app.report import ZProcessReport
from rt.zps.streams import zprint
from rt.zps.tests.mocks import Process
import unittest


class TestZps(unittest.TestCase):
    '''
    Test zps
    '''
    def testZProcessReport_init(self):
        '''
        We take the mock process and see what happens
        '''
        pr = ZProcessReport(Process())
        # I add a couple of newlines for aestetich reasons
        print ("\n\n")
        zprint(str(pr))

if __name__ == '__main__':
    unittest.main()
