#!/usr/bin/env python3

# Wait for GPIO pin 7 to get grounded, then shut the machine down.
# args: [--test]

from datetime import datetime
from gpiozero import Button
import os
import signal
import sys
import time


testing_ = False
if len(sys.argv) == 2 and sys.argv[1] == '--test':
  testing_ = True
  print('Running in test mode')


# Handler for SIGUSER1, which does nothing!
#def handleSignal(num, stack):
#  print('Got signal! And now we mysteriously will exit....')
#  return


def logMessage(msg):
  fullmsg = '{}: {} @ {}'.format(sys.argv[0], msg, datetime.now())
  # os.system('sudo logger -p emerg "{}"'.format(msg))
  opt = ''
  if not testing_:
    opt = '-p emerg'
  os.system('sudo logger {} "{}"'.format(opt, fullmsg))


def doShutdown():
  msg = 'POWERING OFF'
  if testing_:
    msg = '(Testing) ' + msg
  logMessage(msg)

  if testing_:
    print('Testing - NOT shutting down')

    # Send a SIGUSER1; this seems to cause signal.pause() to return.
    os.kill(os.getpid(), signal.SIGUSR1)

  else:
    os.system('sudo poweroff')


button = Button(7)
button.when_held = doShutdown

# If we don't catch the signal, we get a message on screen. Big deal.
#if testing_:
  # Install a handler for SIGUSER1 .... which seems to entirly fix our problem. Why?!?!
#  signal.signal(signal.SIGUSR1, handleSignal)

# this waits but we can't get out of it! (sys.exit() doesn't!)
# But it's OK in our real world use, cuz the poweroff command *does* kill everything.
#
print('Waiting for button hold....')
logMessage('Installed poweroff button handler.')
signal.pause()

