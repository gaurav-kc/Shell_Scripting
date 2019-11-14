#!/bin/bash
if ! [ -d $1 ] ;
then
	echo "Invalid"
	exit -1
fi
case $# in
	2)	#2args
		case $2 in
			all)	
				cd $1
				temp2=$(ls | grep -o "\..*" | grep -o "[A-Za-z0-9_]*" | sort -u)
				for i in $temp2 ; do
   					temp="$i"
#					echo "$i"
   					mkdir -p $temp
   					mv *.$temp $temp
				done
				exit 0
			;;
			*)	
				cd $1
#				echo "$1 ... $2"
				mkdir -p $2
				mv *.$2 $2
				exit 0
			;;
		esac
	;;
	*)	
		i=2
		for i in "$@"
		do
  			cd $1
  			mkdir -p $i
  			mv *.$i $i
		done
		exit 0
	;;
esac
exit -1

