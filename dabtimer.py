""" This is the docstring.
"""
import time

######################################################################
## TIMER CLASS
class DABTimer():
    """ This is the docstring.
    """
    def __init__(self):
        self._time_cpu_prev = time.process_time()
        self._time_wallclock_begin = time.time()
        self._time_wallclock_prev = self._time_wallclock_begin

######################################################################
##
    def timecall(self, label):
        """ This is the docstring.
        """
        time_cpu_next = time.process_time()
        time_wallclock_next = time.time()
        time_cpu = time_cpu_next - self._time_cpu_prev
        time_wallclock_current = time_wallclock_next - \
                   self._time_wallclock_prev
        time_wallclock_total = time_wallclock_next - \
                   self._time_wallclock_begin

        if time_wallclock_current > 0.0:
            percent = 100.00 * (time_cpu / time_wallclock_current)
            if percent > 100.00:
                percent = 100.00
        else:
            percent = 100.00

        outstring = 'TIME*******************************************************************\n'
        outstring += 'TIME %-20s %7.3f  %10.3f user   %10.3f wall\n' % \
                     (label, percent, time_cpu, time_wallclock_current)
        outstring += 'TIME %-20s          %10.3f user_t %10.3f wall_t\n' % \
                     (label, time_cpu_next, time_wallclock_total)
        outstring += 'TIME*******************************************************************'

        self._time_cpu_prev = time_cpu_next
        self._time_wallclock_prev = time_wallclock_next

        # return the output string
        # and [cpu time of this interval,  cpu time total]
#        return outstring, [time_cpu, time_cpu_next]
        return outstring
