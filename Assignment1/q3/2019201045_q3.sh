i=0
temp2=$1
while [ $i -lt ${#temp2} ] && [ ${temp2:$i:1} != "." ] ; do
	(( i++ ))
done
(( i++ ))
while [ $i -lt ${#temp2} ] ; do
		tp="${tp}${temp2:$i:1}"
		(( i++ ))
done
case $tp in
	tar)
		tar -xvf $1
	;;
	tar.gz)
		tar -xvzf $1
	;;
	tar.bz2)
		tar -xvjf $1
	;;
        tar.xz)
		tar xf $1
	;;
	tgz)
		tar zxvf $1
	;;
	tbz2)
		tar -jxvf $1
	;;
	bz2)
		bzip2 $1
	;;
	zip)
		unzip $1
	;;
	7z)
		7z x $1
	;;
	gz)
		gunzip $1
	;;
esac	
