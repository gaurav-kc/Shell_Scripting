#!/bin/bash

if [ $# -ne 1 ] ;
then
	echo "Please provide one filename"
	exit -1
fi
if ! [ -e $1 ] ;
then
	echo "File doesn't exist"
	exit -2
fi 
if ! [ -r $1 ] ;
then
	echo "Reading permission denied"
	exit -3
fi
if ! [ -w $1 ] ;
then
	echo "File opening in read-only mode"
fi
temp2=$( file --mime-type $1 )
#echo "one $temp2"
i=0
while [ $i -lt ${#temp2} ] && [ ${temp2:$i:1} != ":" ] ; do
	(( i++ ))
done
(( i+=2 ))
while [ $i -lt ${#temp2} ] ; do
		tp="${tp}${temp2:$i:1}"
		(( i++ ))
done
#echo "1.5 $tp"
temp4=$(cat /usr/share/applications/defaults.list | grep "$tp")
#echo "two $temp4"
i=0
while [ $i -lt ${#temp4} ] && [ ${temp4:$i:1} != "=" ] ; do
	(( i++ ))
done
(( i++ ))
while [ $i -lt ${#temp4} ] ; do
		tp1="${tp1}${temp4:$i:1}"
		(( i++ ))
done	
#echo $tp1
temp5=$(cat /usr/share/applications/$tp1 | grep "Exec")
i=0
while [ $i -lt ${#temp5} ] && [ ${temp5:$i:1} != "=" ] ; do
	(( i++ ))
done
(( i++ ))
while [ $i -lt ${#temp5} ] && [ ${temp5:$i:1} != " " ] ; do
		tp2="${tp2}${temp5:$i:1}"
		(( i++ ))
done	
echo $tp2
if ! [ "$tp2" = "" ] ;
then
	$tp2 $1
else
	i=0
	type=""
	while [ $i -lt ${#tp} ] && [ ${tp:$i:1} != "/" ] ; do
		type="${type}${tp:$i:1}"
		(( i++ ))
	done
	case $type in
		text)
			/usr/bin/gedit $1
		;;
		audio)
			/usr/bin/rhythmbox $1
		;;
		image)
			/usr/bin/eog $1
		;;
		video)
			/usr/bin/totem $1
		;;
		*)
			echo "Not found"
		;;
	esac
fi
