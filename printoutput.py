""" This is the docstring.
"""
OUTFILE = None
LOGFILE = None
######################################################################
##     Prints 'outstring' to 'stdout' and to 'outfile'.
def printoutput(outstring, outfile):
    """ This is the docstring.
    """
    print(outstring)
    outfile.write('%s\n' % (outstring))
    outfile.flush()
