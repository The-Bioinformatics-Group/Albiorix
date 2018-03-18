#!/bin/env python

import subprocess
import os
backupSize = subprocess.Popen("df /BACKUP", shell=True, stdout=subprocess.PIPE).stdout.read().split()

if int(backupSize[11].rstrip("%")) == 100:
	os.system('echo "$(tput setab 1)The BACKUP file system is full.$(tput sgr 0)"')
	os.system('echo "$(tput setab 1)No new data will be backed up until more space is made available.$(tput sgr 0)"')
else:
	os.system('echo "$(tput setab 4)Data stored in your HOME directory and under /proj/dataX is backed up.$(tput sgr 0)"')


#if homeSize[-1] == "G" and homeSize[:-1] >= "200":
#	os.system('echo "$(tput setab 1)You have %s of data in your HOME directory.$(tput sgr 0)"' % homeSize)
#	os.system('echo "$(tput setab 1)Please decrease your disk usage to <200G.$(tput sgr 0)"')
#
#else:
#	os.system('echo "$(tput setab 4)You have %s of data in your HOME directory.$(tput sgr 0)"' % homeSize)
