#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Raspberry PI
Check to see if there is a valid IP Address
If Not, then down/up wlan0 and check again.
Jose F. Reyes
Jan 16, 2016 @23:32
'''
import commands
import datetime
import time

class network():
    def reset(self):
        f = open('/home/pi/jose/RoboRaspi/network_check/ip_check.txt', 'a')
        now = datetime.datetime.now()
        f.write('\n')
        f.write(str(now))
        f.write('\n')
        f.write("Running Network.Reset() Function")
        f.write('\n')
        self.restart = commands.getoutput("sudo ifdown wlan0 && sudo ifup wlan0")
        f.write("Restart executed, waiting 10 seconds before checking again")
        f.write('\n')
        time.sleep(10)
        f.write("Checking IP after reset")
        f.write('\n')
        ip_address = commands.getoutput("hostname -I")
        try:
            if "192.168.1." not in ip_address:
                f.write("IP Address still invalid, wait 10s then run Reset() Again...")
                time.sleep(10)
                self.reset()
            else:
                f.write("IP Address successfully Reset!")
                f.write('\n')
                f.write(ip_address)
                f.write('\n')
                f.write("=======================")
        except ValueError:
            pass
        f.close()
now = datetime.datetime.now()
f = open('/home/pi/jose/RoboRaspi/network_check/ip_check.txt', 'a')
f.write('\n')
f.write(str(now))
f.write('\n')
f.write("Checking if we have a valid IP Address")
f.write('\n')
ip_address = commands.getoutput("hostname -I")
try:
    if "192.168.1" not in ip_address:
        f.write("IP Address Invalid... Attempting to reset() ")
        f.write('\n')
        f.close()
        A = network()
        A.reset()
    else:
        print ip_address, "is a valid IP Address"
        f.write("IP Address is Valid")
        f.write('\n')
        f.write(ip_address)
        f.write('\n')
        f.write("-------------------------")
        f.write('\n')
        f.close()
except AttributeError:
    pass
