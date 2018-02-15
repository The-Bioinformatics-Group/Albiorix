#!/bin/bash
w|cut -f1 -d " "|grep -v "USER"|uniq|sed '/^\s*$/d'|wc -l
