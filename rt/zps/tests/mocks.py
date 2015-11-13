# -*- coding: utf-8 -*-
from rt.zps.tests import __path__ as zps_test_path
try:
    from psutil import AccessDenied
except ImportError:
    # psutil < 2.0.0
    from psutil.error import AccessDenied


class Process(object):
    '''
    This is a mock object for zps unit tests
    '''
    username = 'plone'
    pid = 1111
    fake_memory_percent = 1.23
    cwd = '/a/path'

    @property
    def cmdline(self):
        '''
        Return the commandline for this process
        '''
        zope_path = zps_test_path[0] + '/0zope.conf'
        return ['program', zope_path]

    def get_memory_percent(self):
        '''
        Return a float
        '''
        return self.fake_memory_percent

    def getcwd(self):
        '''
        Return the current workind directory
        '''
        return self.cwd


class DeniedProcess(Process):
    '''
    This process raises an AccessDenied while getting the cwd
    '''
    def getcwd(self):
        '''
        Return the current workind directory
        '''
        raise AccessDenied
