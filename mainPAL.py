#!/usr/bin/env python
""" This is the docstring.
"""
import sys
from turingmachine import TM
import config
from myargparse import parseargs
from printoutput import printoutput
from dabtimer import DABTimer

############################################################################
## main function
def main(which, infilename):
    """ This is the docstring.
    """

    ########################################################################
    ## Measure process and wall clock times.
    dabtimer = DABTimer()
    logstring = dabtimer.timecall('BEGINNING')
    printoutput(logstring, config.LOGFILE)

    thistm = TM()
    thistm.read(which)
    infile = open(infilename)
    for line in infile:
        startString = "\nSTART "+which+'\n***********************************************************************'
        printoutput(startString, config.LOGFILE)

        line = line.strip()
        tape = list(line)
        tapeheadpos = 1
        tape = thistm.execute(tape, tapeheadpos)

        finalState = thistm.getFinalState()
        endString = "FINAL "+which+" STATE REACHED, HALT AND ACCEPT " if finalState != 'FAILSTATE' else "FAILURE "+which+" STATE REACHED, HALT AND REJECT "
        endString += thistm.getEndTape()
        endString += "\n***********************************************************************\n"
        printoutput(endString, config.LOGFILE)

    infile.close()

    logstring = dabtimer.timecall('ENDING')
    printoutput(logstring, config.LOGFILE)

############################################################################
## main Main MAIN
if __name__ == '__main__':
    OPTIONS = parseargs([['-w', '--which', 'which'],
                         ['-i', '--infilename', 'infilename'],
                         ['-l', '--logfilename', 'logfilename']
                         ])
    config.LOGFILE = open(OPTIONS.logfilename, 'w')
    printoutput(f'OPTIONS {OPTIONS}', config.LOGFILE)
    main(OPTIONS.which, OPTIONS.infilename)
