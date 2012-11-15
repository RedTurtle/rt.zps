# -*- coding: utf-8 -*-
from sys import stdout, stderr


def zprint(text):
    '''
    Function used to print text
    '''
    return stdout.write(text)


def zerror(text):
    '''
    Function used to print text
    '''
    return stderr.write(text)


def zfatalerror(text):
    """
    Outputs text on stderr and then exits
    """
    zerror(text)
    return exit()
