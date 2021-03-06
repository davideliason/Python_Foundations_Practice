#!/usr/bin/env python3
import shutil
import psutil
# import custom network module
from network import *

def check_disk_usage(disk):
     du = shutil.disk_usage(disk)
     free = du.free / du.total * 100
     return free > 20

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 75

# script to check if either function returns false value

if not check_disk_usage("/") or not check_cpu_usage():
	print("Error!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
print("network checks failed")

# to run
# in terminal: chmod + x automate_diskuage_cpu.py
# $./automate...
