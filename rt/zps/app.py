# -*- coding: utf-8 -*-
import psutil, sys, getopt

__usage__ = """
USAGE:
  zps
  zps --help
  zps --pid 1111
  zps --port 8080
""".lstrip()

__doc__ = ("""
zps - report a snapshot of the current zope processes.

%s
""" % __usage__).lstrip()

PID_ERROR = "pid value must be an integer number\n\n" + __doc__
REPORT_TEMPLATE=''
def onerror(msg):
    """
    Outputs msg and then exits
    """
    sys.stderr.write(msg)
    return sys.exit()

def checkopt():
    """
    Checking command line options
    """
    flags={'pid': 0, 'port': ''}    
    opt_short=''
    opt_long=['pid=', 'port=']
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], opt_short, opt_long)
    except getopt.GetoptError, e:
        onerror("ERROR: %s\n\n%s"%(e, __usage__))
    for opt, optarg in opts:
        if opt == '--pid':
            if not optarg.isdigit():
                onerror(PID_ERROR)
            flags['pid'] = int(optarg)
        if opt == '--port':
            flags['port'] = optarg
    return opts, args, flags

opts, args, flags = checkopt()

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
    
    def getzoncf(self):
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
        return REPORT_TEMPLATE % self
        
class ZProcessFinder(object):
    """
    This object finds out the processes run by zope
    """
    def __init__(self):
        """
        Initialize this object with flags
        """
        
    @property    
    def plist(self):
        """
        This is the list of processes this object is aware of
        """
        plist = []
        for p in psutil.get_process_list():
            pstr = "".join(p.cmdline)
            if 'zope.conf' in pstr:
                pdict = ZProcessReport(p)
                if ((not flags['pid'] or (int(flags['pid']) == pdict['pid'])) 
                    and flags['port'] in pdict['address']):
                    plist.append(pdict)
        return plist

    def __str__(self):
        """
        Returns the output message with info about zope processes
        """
        plist = self.plist
        if not plist:
            return "No running zope instance found"
        return "\n".join(map(str, plist))
