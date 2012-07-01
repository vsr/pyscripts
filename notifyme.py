#!/usr/bin/python
"""
Notifies with a fortune cookie every X minutes.
Usage: "python notifyme.py 10" to notify every 10 minutes
"""

import os
import sys
import datetime
import time
import pynotify


def notify(count):
    fortune = os.popen('fortune -n 100 -s', 'r').read()
    time = datetime.datetime.now().strftime("%H:%M:%S")
    pynotify.Notification("%s (%s) >>" % (time, count), fortune).show()


if __name__ == "__main__":
    pynotify.init('Notify Me')
    try:
        interval = float(sys.argv[1])
    except:
        interval = 20
    notification_count = 0
    try:
        while True:
            notification_count += 1
            notify(notification_count)
            time.sleep(interval * 60)
    except (KeyboardInterrupt, SystemExit):
        print "\nNotified %s times." % notification_count
        exit
