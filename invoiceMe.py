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
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose", default=False)
parser.add_argument("-d", "--days", action="store", help="Number of days to report statistics from [30].", default=30)
parser.add_argument("-s", "--seconds", action="store_true", help="Report statistics in seconds.", default=False)
parser.add_argument("-c", "--cpu", action="store_true", help="Show total CPU usage.")
parser.add_argument("-q", "--queue", action="store_true", help="Show statistics per queue.")
parser.add_argument("-u", "--user", action="store", help="User to show statistics for [$USER].", default="$USER")
parser.add_argument("-g", "--group", action="store", help="Group to show statistics for.", default="Primary_group")
parser.add_argument("-p", "--price", action="store_true", help="Calculate the price for the used resources.")
parser.add_argument("--debug", action="store_true", help="Only used during development.")
args = parser.parse_args()

# Amazon Virtual server (EC2) prices




class Stats(object):
	def __init__(self, raw_stats):

#		print "raw_stats: ", raw_stats			# Devel.
		self.stats = raw_stats
		try:
#		print self.stats[0].split()[1]			# Devel.
			self.user = self.stats[0].split()[1]
		except IndexError:
			sys.exit("No statistics available for user %s for the last %s days." % (args.user, args.days))
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
		### Debug ###
		if args.debug == True:
			print self.cpu_time
		out = ""
		for queue in self.cpu_time:
			if args.verbose:
				out += str(queue[0])
				out += " "
				if args.seconds:
					out += str(round(float(queue[1]), 1)) + " seconds" + "\n"
				else:
					out += str(round(float(queue[1])/60/60, 1)) + " hours" + "\n"
			else:
				if args.seconds:
					out += str(round(float(queue[1]), 1)) + "\n"
				else:
					out += str(round(float(queue[1])/60/60, 1)) + "\n"
#			if args.seconds == True:
#				out += str(queue[0]) + " " + str(round(float(queue[1]), 1)) + " seconds" + "\n"
#			else:
#				out += str(queue[0]) + " " + str(round(float(queue[1])/60/60, 1)) + " hours" + "\n"
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
	if args.group == "Primary_group":
		my_group_out = subprocess.Popen(["groups %s" % args.user], stdout=subprocess.PIPE, shell=True)
		my_group = my_group_out.communicate()[0]
		group = my_group.split(":")[1].split()[0]
	else:
		group = args.group
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
	if args.cpu:
		if args.verbose == True:
			print "[Total CPU usage last %s days]" % args.days
		print user.get_total_cpu()
		print group.get_total_cpu()
	if args.queue:
		if args.verbose == True:
			print "[CPU usage per queue the last %s days]" % args.days
			print "[User %s]" % args.user
		print user.get_per_queue_cpu()
		if args.verbose == True:
			print "[Group %s]" % group.get_user()
		print group.get_per_queue_cpu()




if __name__ == "__main__":
    main()
