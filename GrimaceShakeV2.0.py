import time
#Import Libraries Here
#Import time
import sys

timeToSleep = 3

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsis add a dot .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message =("InInfoTech Center Operating System Booting" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # /r prints carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print ("\n\nOperating Syatem Booted up - Retina Scanned - Access Granted!")
