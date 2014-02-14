# -*- coding: utf-8 -*-
import re
from os.path import isfile
from psutil.error import AccessDenied
from rt.zps.templates.report import REPORT_TEMPLATE
from rt.zps.streams import zerror

HTTP_SERVER_PATTERN = re.compile('<http-server>(.*)</http-server>', re.S)
ZEO_SERVER_PATTERN = re.compile('<zeo>(.*)</zeo>', re.S)
ADDRESS_PATTERN = re.compile('(\s*)address(\s*)(\d|\.|\:)+')
PBASE_PATTERN = re.compile('(\s*)port-base(\s*)(\d)*')


class ZProcessReport(dict):
    '''
    The Zope process report class
    '''
    process = None
    zconf = None

    def __init__(self, process):
        """
        This reports on a zope process
        """
        self.process = process
        self.get_report_data()

    def get_report_data(self):
        '''
        Reads process and zope configuration file data to fill the report
        '''
        zconf = self.getzconf()
        if not zconf:
            return
        # Process data
        self['cwd'] = self.getcwd()
        self['user'] = self.process.username
        self['pid'] = self.process.pid
        self['memory'] = "%.2f%%" % self.process.get_memory_percent()
        # Zope data
        self['zconf'] = zconf
        self['address'] = self.getport()

    def __str__(self):
        """
        String representation of my process
        """
        try:
            return REPORT_TEMPLATE.substitute(self)
        except:
            return ''

    def getcwd(self):
        '''
        Get the current working directory from the process. I found this
        information missing on a Leopard installation
        '''
        try:
            return self.process.getcwd()
        except AccessDenied:
            return "Access denied"
        except AttributeError:
            return "Information not available on this platform"

    def getzconf(self):
        """
        Try to the the zope configuration file
        """
        for x in self.process.cmdline:
            if (('zope.conf' in x or 'zeo.conf' in x) and isfile(x)):
                return x

    def lineparser(self, line, target):
        """
        Parses a line containing target
        """
        if target in line:
            line = line.strip()
            if line.startswith(target):
                return line.replace(target, '').strip()
        return False

    def getport(self):
        """
        Tries to get the port of the running zope instance parsing the zope
        configuration file
        """
        zconf = open(self['zconf']).read()
        http_server = HTTP_SERVER_PATTERN.search(zconf)

        if http_server:
            address = ADDRESS_PATTERN.search(http_server.group(0))
            if address:
                address = self.lineparser(address.group(0), 'address')
            else:
                return "No address found"

            pbase = PBASE_PATTERN.search(http_server.group(0))
            if pbase:
                pbase = int(self.lineparser(pbase.group(0), 'port-base'))
            else:
                pbase = 0
        else:
            return 'No http-server section found'

        if ':' in address:
            host, port = address.split(':')
        else:
            host, port = '0.0.0.0', address
        try:
            port = str(int(port) + int(pbase))
        except Exception as e:
            zerror(str(e))
            return ''
        return ':'.join((host, port))
