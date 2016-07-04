#!/bin/env python

import subprocess
import os
homeSize = subprocess.Popen("du -hs /home/$USER", shell=True, stdout=subprocess.PIPE).stdout.read().split()[0]
os.system('echo "$(tput setab 4)You have %s of data in your HOME directory.$(tput sgr 0)"' % homeSize)
