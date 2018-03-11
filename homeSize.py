#!/bin/env python

import subprocess
import os
homeSize = subprocess.Popen("du -hs /home/$USER", shell=True, stdout=subprocess.PIPE).stdout.read().split()[0]

if homeSize[-1] == "G" and homeSize[:-1] >= "200":
	os.system('echo "$(tput setab 1)You have %s of data in your HOME directory.$(tput sgr 0)"' % homeSize)
	os.system('echo "$(tput setab 1)Please decrease your disk usage to <200G.$(tput sgr 0)"')

else:
	os.system('echo "$(tput setab 4)You have %s of data in your HOME directory.$(tput sgr 0)"' % homeSize)
