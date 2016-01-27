#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Raspberry PI
Check to see if there is a valid IP Address
If Not, then down/up wlan0 and check again.
Jose Reyes | yanks81@gmail.com
Jan 18, 2016 @19:43
'''
import commands
import datetime
import time
from pytz import timezone

class network():
    def reset(self):
        f = open('/home/pi/network_check/network.log', 'a')
        fmt = "%Y-%m-%d %H:%M:%S %Z%z"
        now_utc = datetime.datetime.now(timezone('UTC'))
        now_eastern = now_utc.astimezone(timezone('US/Eastern'))
        now = now_eastern.strftime(fmt)

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
                f.write("-------------------------")
        except ValueError:
            pass
        f.close()

fmt = "%Y-%m-%d %H:%M:%S %Z%z"
now_utc = datetime.datetime.now(timezone('UTC'))
now_eastern = now_utc.astimezone(timezone('US/Eastern'))
now = now_eastern.strftime(fmt)
f = open('/home/pi/network_check/network.log', 'a')
f.write('\n')
f.write(str(now))
f.write('\n')
f.write("Checking for valid IP Address")
f.write('\n')
ip_address = commands.getoutput("hostname -I")
try:
    if "192.168.1" not in ip_address:
        f.write("IP Address Invalid; Calling reset() ")
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
