#!/bin/bash

# Create mountpoints on the login server
mkdir -p /nobackup/data1
mkdir -p /proj/data2
mkdir /nobackup/data3
mkdir /proj/data4
mkdir /proj/data5
mkdir /proj/data6
mkdir /nobackup/data7
mkdir /proj/data8
mkdir /proj/data9
mkdir /nobackup/data10
mkdir /proj/data11
mkdir /nobackup/data12
mkdir /proj/data13
mkdir /proj/data14
mkdir /proj/data15
mkdir /proj/data16
mkdir /proj/data17
mkdir /nobackup/data18
mkdir /proj/data19
mkdir /proj/data20
mkdir /proj/data21
mkdir /proj/data22
mkdir /proj/data23
mkdir /nobackup/data24
mkdir /proj/data25

# Mount the NAS disks on the login server
mount nas-0-0:/export/data1 /nobackup/data1
mount nas-0-0:/export/data2 /proj/data2
mount nas-0-0:/export/data3 /nobackup/data3
mount nas-0-0:/export/data4 /proj/data4
mount nas-0-0:/export/data5 /proj/data5
mount nas-0-0:/export/data6 /proj/data6
mount nas-0-0:/export/data7 /nobackup/data7
mount nas-0-0:/export/data8 /proj/data8
mount nas-0-0:/export/data9 /proj/data9
mount nas-0-0:/export/data10 /nobackup/data10
mount nas-0-0:/export/data11 /proj/data11
mount nas-0-0:/export/data12 /nobackup/data12
mount nas-0-0:/export/data13 /proj/data13
mount nas-0-0:/export/data14 /proj/data14
mount nas-0-0:/export/data15 /proj/data15
mount nas-0-0:/export/data16 /proj/data16
mount nas-0-0:/export/data17 /proj/data17
mount nas-0-0:/export/data18 /nobackup/data18
mount nas-0-0:/export/data19 /proj/data19
mount nas-0-0:/export/data20 /proj/data20
mount nas-0-0:/export/data21 /proj/data21
mount nas-0-0:/export/data22 /proj/data22
mount nas-0-0:/export/data23 /proj/data23
mount nas-0-0:/export/data24 /nobackup/data24
mount nas-0-0:/export/data25 /proj/data25

# Create mountpoints on the compute nodes
rocks run host "mkdir -p /nobackup/data1"
rocks run host "mkdir -p /proj/data2"
rocks run host "mkdir /nobackup/data3"
rocks run host "mkdir /proj/data4"
rocks run host "mkdir /proj/data5"
rocks run host "mkdir /proj/data6"
rocks run host "mkdir /nobackup/data7"
rocks run host "mkdir /proj/data8"
rocks run host "mkdir /proj/data9"
rocks run host "mkdir /nobackup/data10"
rocks run host "mkdir /proj/data11"
rocks run host "mkdir /nobackup/data12"
rocks run host "mkdir /proj/data13"
rocks run host "mkdir /proj/data14"
rocks run host "mkdir /proj/data15"
rocks run host "mkdir /proj/data16"
rocks run host "mkdir /proj/data17"
rocks run host "mkdir /nobackup/data18"
rocks run host "mkdir /proj/data19"
rocks run host "mkdir /proj/data20"
rocks run host "mkdir /proj/data21"
rocks run host "mkdir /proj/data22"
rocks run host "mkdir /proj/data23"
rocks run host "mkdir /nobackup/data24"
rocks run host "mkdir /proj/data25"

# Mount the NAS disks on the compute nodes
rocks run host "mount nas-0-0:/export/data1 /nobackup/data1"
rocks run host "mount nas-0-0:/export/data2 /proj/data2"
rocks run host "mount nas-0-0:/export/data3 /nobackup/data3"
rocks run host "mount nas-0-0:/export/data4 /proj/data4"
rocks run host "mount nas-0-0:/export/data5 /proj/data5"
rocks run host "mount nas-0-0:/export/data6 /proj/data6"
rocks run host "mount nas-0-0:/export/data7 /nobackup/data7"
rocks run host "mount nas-0-0:/export/data8 /proj/data8"
rocks run host "mount nas-0-0:/export/data9 /proj/data9"
rocks run host "mount nas-0-0:/export/data10 /nobackup/data10"
rocks run host "mount nas-0-0:/export/data11 /proj/data11"
rocks run host "mount nas-0-0:/export/data12 /nobackup/data12"
rocks run host "mount nas-0-0:/export/data13 /proj/data13"
rocks run host "mount nas-0-0:/export/data14 /proj/data14"
rocks run host "mount nas-0-0:/export/data15 /proj/data15"
rocks run host "mount nas-0-0:/export/data16 /proj/data16"
rocks run host "mount nas-0-0:/export/data17 /proj/data17"
rocks run host "mount nas-0-0:/export/data18 /nobackup/data18"
rocks run host "mount nas-0-0:/export/data19 /proj/data19"
rocks run host "mount nas-0-0:/export/data20 /proj/data20"
rocks run host "mount nas-0-0:/export/data21 /proj/data21"
rocks run host "mount nas-0-0:/export/data22 /proj/data22"
rocks run host "mount nas-0-0:/export/data23 /proj/data23"
rocks run host "mount nas-0-0:/export/data24 /nobackup/data24"
rocks run host "mount nas-0-0:/export/data25 /proj/data25"

# Mount /usr/local
rocks run host "mv /usr/local /usr/rocks.local"
rocks run host "ln -s /home/local /usr/local"

####
# Desperate hacks
###

# Make FALCON work again
rocks run host "mount nas-0-0:/export/data5 /nobackup/data5"
