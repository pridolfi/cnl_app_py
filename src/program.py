#!/usr/bin/python

import wiringpi
import time
import sdnotify

OUTPUT = 21

n = sdnotify.SystemdNotifier()
n.notify("READY=1")

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(OUTPUT, 1)

while True:
    wiringpi.digitalWrite(OUTPUT, 1)
    time.sleep(2)
    wiringpi.digitalWrite(OUTPUT, 0)
    time.sleep(2)
    n.notify("WATCHDOG=1")
