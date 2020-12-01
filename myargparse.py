""" This is the docstring.
"""
######################################################################
## This is my version of an argument parser.
import sys
import configargparse

######################################################################
## PARSE ARGUMENTS
def parseargs(arglist):
    p = configargparse.ArgParser(default_config_files=['config.txt'])
    p.add('-c', is_config_file=True, help='configfilename') 
    for onearg in arglist:
        argshort = onearg[0]
        arglong = onearg[1]
        helpinfo = onearg[2]
        p.add(argshort, arglong) 
    options = p.parse_args()
    optionsstr = f'{str(options)}'.replace('(c=None', '')
    optionsstr = optionsstr.replace(' c=None', '')
    if '=None' in optionsstr:
        optionsstr = f'{str(options)}'
        print('ERROR--arguments missing', optionsstr)
        sys.exit()

    return options
