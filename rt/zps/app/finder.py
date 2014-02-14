# -*- coding: utf-8 -*-
import psutil
from rt.zps.app.report import ZProcessReport
from rt.zps.streams import zprint
from rt.zps.templates.usage import USAGE


class ZProcessFinder(object):
    """
    This object finds out the processes run by zope
    """
    def __init__(self, flags):
        """
        Initialize this object with flags
        """
        self.flags = flags

    def process_commandline(self, p):
        '''
        Returns the commandline of a psutil process
        '''
        return "".join(p.cmdline)

    def p2dict(self, p):
        '''
        Checks if a process is one we care about
        '''
        pstr = self.process_commandline(p)
        if not ('zope.conf' in pstr or 'zeo.conf' in pstr):
            return

        flags = self.flags
        if flags['grep'] and not flags['grep'] in pstr:
            return
        pdict = ZProcessReport(p)
        if (flags['pid'] and int(flags['pid']) != pdict['pid']):
            return
        if flags['port'] and not flags['port'] in pdict['address']:
            return
        return pdict

    @property
    def plist(self):
        """
        This is the list of processes this object is aware of
        """
        pdicts = []
        for process in psutil.process_iter():
            pdict = self.p2dict(process)
            if pdict:
                pdicts.append(pdict)
        pdicts.sort(key=lambda x: x['zconf'])
        return pdicts

    def __str__(self):
        """
        Returns the output message with info about zope processes
        """
        if self.flags['help']:
            return USAGE
        plist = self.plist
        if not plist:
            return "No running zope instance found\n"
        return "\n".join(map(str, plist))

    def __call__(self):
        '''
        When called output it's string representation
        '''
        zprint(str(self))
