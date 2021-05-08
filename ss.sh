#!/bin/sh

#WORD='script'
#echo "I want to be good in ${WORD}ing!"


#WORD='read'
#echo "I want to be good in ${WORD}ing!"

#This script displays information about system on which it runs.
echo "Person executint this script is ${UID}"

#Tell user the script is running
echo 'Script is running'


#Display the hostname of the user
hostname


#Display the current date and time this iformation collected
date

#Kernel Release followed by Architecture.
uname -r 
uname -m 

#Display the disk usuage in human readable form.
df -h

#Done
echo "Done"


