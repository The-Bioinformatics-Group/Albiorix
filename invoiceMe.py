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
														        
parser = argparse.ArgumentParser(prog="invoiceMe.py")
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
parser.add_argument("-d", "--days", action="store", help="Number of days to report statistics from.", default=30)
parser.add_argument("-s", "--seconds", action="store_true", help="Report statistics in seconds.", default=False)
parser.add_argument("-c", "--cpu", action="store_true", help="Show total CPU usage.")
parser.add_argument("-q", "--queue", action="store_true", help="Show statistics per queue.")
parser.add_argument("-u", "--user", action="store", help="User to show statistics for.", default="$USER")
parser.add_argument("-g", "--group", action="store", help="Group to show statistics for.", default="Primary_group")
args = parser.parse_args()

# Amazon Virtual server (EC2) prices




class Stats(object):
	def __init__(self, raw_stats):
		self.stats = raw_stats
		self.user = self.stats[0].split()[1]
		self.wallclock = []
		self.user_time = []
		self.system_time = []
		self.cpu_time = []
		self.memory = []
		self.IO = []
		self.IOW = []

		for queue in self.stats[:-1]:
			self.queue_name = queue.split()[0]
			self.wallclock.append( (self.queue_name, queue.split()[2]) )
			self.user_time.append( (self.queue_name, queue.split()[3]) )		# User or group
			self.system_time.append( (self.queue_name, queue.split()[4]) )
			self.cpu_time.append( (self.queue_name, queue.split()[5]) )
			self.memory.append( (self.queue_name, queue.split()[6]) )
			self.IO.append( (self.queue_name, queue.split()[7]) )
			self.IOW.append( (self.queue_name, queue.split()[8]) )

	def get_user(self):
		return self.user

	def get_wallclock(self):
		return self.wallclock

	def get_total_cpu(self):
		# Return the total CPU usage 
		self.total = 0
		self.out = ""
		if args.verbose:
			self.out += str(self.get_user())
			self.out += " " 
		for queue in self.cpu_time:
			self.total += float(queue[1])
		if args.seconds == True:
			self.out += str(self.total)
			if args.verbose:
				self.out += " seconds"
		else:
			self.out += str(round(self.total/60/60, 1))
			if args.verbose:
				self.out += " hours"
		return self.out
	
			
	
	def get_per_queue_cpu(self):
		out = ""
		for queue in self.cpu_time:
			if args.seconds == True:
				out += str(queue[0]) + " " + str(round(float(queue[1]), 1)) + " seconds" + "\n"
			else:
				out += str(queue[0]) + " " + str(round(float(queue[1])/60/60, 1)) + " hours" + "\n"
		return out.rstrip()

	def get_memory(self):
		return self.memory

def user_stats(days):
	out_owner = subprocess.Popen(["qacct -o %s -q -d %s" % (args.user, days)], stdout=subprocess.PIPE, shell=True)
	stats_owner = out_owner.communicate()
#	print stats_owner[0].split("\n")[2:]			# Devel.
	return Stats(stats_owner[0].split("\n")[2:])

def group_stats(days):
	# Figure out the primary group if not set
#	if args.group == "Primary_group":
	my_group_out = subprocess.Popen(["groups $USER"], stdout=subprocess.PIPE, shell=True)
	my_group = my_group_out.communicate()[0]
	group = my_group.split(":")[1].split()[0]
#	else:
	out_group = subprocess.Popen(["qacct -g %s -d %s -q" % (group, days)], stdout=subprocess.PIPE, shell=True)
	stats_group = out_group.communicate()
	return Stats(stats_group[0].split("\n")[2:])


def main():
	# Grab the stats for the last 30 days from the system

	# User
	user = user_stats(args.days)
	# Group
	group = group_stats(args.days)

	# Print result to STDOUT
#	if args.verbose:
#		print(user.get_user()),

	print args.group

	if args.cpu:
		print user.get_total_cpu()
#		print group.get_total_cpu()
	if args.queue:
		print user.get_per_queue_cpu()
#		print group.get_per_queue_cpu()




if __name__ == "__main__":
    main()
