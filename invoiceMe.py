#!/usr/local/opt/python/bin/python

import sys
import subprocess

try:
    import argparse
except ImportError:
	sys.stderr.write("[Error] The python module 'argparse' is not installed\n")
	sys.stderr.write("[--] Would you like to install it now using 'sudo easy_install' [Y/N]? ")
	answer = sys.stdin.readline()
	if answer[0].lower() == "y":
		sys.stderr.write("[--] Running 'sudo easy_install argparse'\n")
		from subprocess import call
		call(["sudo", "easy_install", "argparse"])
	else:
		sys.exit("[Error] Exiting due to missing dependency 'argparser'")
														        
parser = argparse.ArgumentParser(prog="ADD-SCRIPT-NAME-HERE")
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
args = parser.parse_args()

class Stats(object):
	def __init__(self, raw_stats):
		self.stats = raw_stats.split()
		self.user = self.stats[0]		# User or group
		self.wallclock = self.stats[1]
		self.user_time = self.stats[2]		# User or group
		self.system_time = self.stats[3]
		self.cpu_time = self.stats[4]
		self.memory = self.stats[5]
		self.IO = self.stats[6]
		self.IOW = self.stats[7]

	def get_user(self):
		return self.user

	def get_wallclock(self):
		return self.wallclock

	def get_cpu(self):
		return self.cpu_time

	def get_memory(self):
		return self.memory

def user_stats(days):
	out_owner = subprocess.Popen(["qacct -o $USER -d %s" % days], stdout=subprocess.PIPE, shell=True)
	stats_owner = out_owner.communicate()
	return Stats(stats_owner[0].split("\n")[2])

def group_stats(days):
	# Figure out the default group
	my_group_out = subprocess.Popen(["groups $USER"], stdout=subprocess.PIPE, shell=True)
	my_group = my_group_out.communicate()[0]
	group = my_group.split(":")[1].split()[0]

	out_group = subprocess.Popen(["qacct -g %s -d 30" % group], stdout=subprocess.PIPE, shell=True)
	stats_group = out_group.communicate()
	return Stats(stats_group[0].split("\n")[2])

def main():
	# Grab the stats for the last 30 days from the system

	# User
	user_month = user_stats(30)
	user_year = user_stats(365)	
	# Group
	group_month = group_stats(30)
	group_year = group_stats(365)

	print "Hi " + user_month.get_user()




if __name__ == "__main__":
    main()
