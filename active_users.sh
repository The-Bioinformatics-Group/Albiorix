#!/bin/bash
# Displays the number of user accounts that has been active during the last 365 day. Temporary student accounst like 'stud*' and 'phylo*' are not counted.

USERS=$(lastlog -t 365|cut -f1 -d " "|uniq|grep -v "stud"|grep -v "phylo"|grep -v "Username"|wc -l)
printf "\n$(tput setab 4)Albiorix has had $USERS active users the last 12 months.$(tput sgr 0)\n"
