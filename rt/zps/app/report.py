# -*- coding: utf-8 -*-
from rt.zps.templates.report import REPORT_TEMPLATE

class ZProcessReport(dict):
    '''
    The Zope process report class
    '''
    def getcwd(self):
        '''
        Get the current working directory from the process. I found this 
        information missing on a Leopard installation
        '''
        try:
            return self.process.getcwd()
        except AttributeError:
            return "Information not available on this platform"
    
    def getzconf(self):
        """
        Try to the the zope configuration file
        """
        for x in self.process.cmdline:
            if 'zope.conf' in x:
                return x
        return ''        
    
    def lineparser(self, line, target):
        """
        Parses a line containing target
        """
        if target in line:
            line=line.strip()
            if line.startswith(target):
                return line.replace(target, '').strip()
        return False
    
    def getport(self):
        """
        Tries to get the port of the running zope instance parsing the zope 
        configuration file
        """
        address = False
        pbase = False
        for line in file(self['zconf']):
            if not address:
                address = self.lineparser(line, 'address')
            if not pbase:
                pbase = self.lineparser(line, 'port-base')
            if address and pbase:
                # we already have all the info we need, it is useless to go on
                break
        try:
            return str(int(address)+int(pbase))
        except Exception, e:
            print str(e)
            return ''
    
    def __init__(self, process):
        """
        This reports on a zope process
        """
        self.process = process
        self['cwd'] = self.getcwd()
        self['user'] = process.username
        self['pid'] = process.pid
        # Trying to get from the commandline the zope configuraton file
        self['zconf'] = self.getzconf()
        # Getting the address information from the zope.configuraton file
        self['address'] = self.getport()
        self['memory'] = "%.2f%%" % process.get_memory_percent()
        
    def __str__(self):
        """
        String representation of my process
        """
        return REPORT_TEMPLATE.substitute(self)
