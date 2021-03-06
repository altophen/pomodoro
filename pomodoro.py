#!/usr/bin/python
# short pomodermo timer that operates independently of the wall clock
# it sounds an alarm twenty minutes after being started.
# and gives a visual indication of how far into the time poriod the user is

# the visual indicator tells numerically how much time total was allotted.
#       how much has elapsed (numerically)

#   how it works: (use cases)
#       user starts the program via command line (no options)
#       program counts down 20 minutes, indicating progress of the countdown then
#       sounds an alarm and abandons the old indicator and starts a new indicator
#       then counts down ten minutes indicating the progress of the countdown then
#       sounds a different alarm, abandoing the last indicator then repeats the proccess         
#

import time
from subprocess import call
import sys
import philtime

def progress(tminfo):
    outputstring = '  {:02d}:{:02d}  |  {:02d}:{:02d}  | {:02d}:00'.format(tminfo.RemainingMinutes,tminfo.RemainingSeconds,tminfo.minutes,tminfo.seconds, tminfo.TotalMinutes)
    return outputstring


while True:
    sys.stdout.write('remaining| elapsed |target' + '\n' + '\r')
    for goElapsed in philtime.timesource(20):
        sys.stdout.write(progress(goElapsed)  + '\r')
        sys.stdout.flush()
    sys.stdout.write(progress(goElapsed) + '\n' + '\r')
    sys.stdout.flush()
    print "end of the pomoderm"
    cmd = "play -qn synth 3 sine 1000"
    call(cmd.split()) 

    for goElapsed in philtime.timesource(5):
        sys.stdout.write(progress(goElapsed)  + '\r')
        sys.stdout.flush()
    sys.stdout.write(progress(goElapsed) + '\n' + '\r')
    sys.stdout.flush()
    print "end of the rest period"
    cmd = "play -qn synth 10 sine 750"
    call(cmd.split())

