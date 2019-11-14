#!/bin/bash
length=${#1}
temp=$1
if [ $length -lt 8 ] ;
then
	echo "Password too small"
	exit -1
fi
status=$(echo "$1" | grep -E "*[0-9]+")
if [ "$status" = "" ] ;
then
	echo "Password has no number"
	exit -2
fi
#status=$(echo "$1" | grep -E ".*[@#$%&*+-=].*")
#if [ "$status" = "" ] ;
#then
#	echo "No Special Character"
#	exit -3
#fi
i=0
found=false
while [ $i -lt $length ] ; do
	if [ "${temp:$i:1}" = "@" ] || [ "${temp:$i:1}" = "#" ] || [ "${temp:$i:1}" = "$" ] || [ "${temp:$i:1}" = "%" ] || [ "${temp:$i:1}" = "&" ] || [ "${temp:$i:1}" = "*" ] || [ "${temp:$i:1}" = "+" ] || [ "${temp:$i:1}" = "-" ] ;
	then
		found=true;
		break;
	fi
	(( i++ ))
done
if [ $found = "false" ] ;
then
	echo "No Special character"
	exit -3
fi
echo "Acceptable"
