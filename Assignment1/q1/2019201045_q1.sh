wget https://darksky.net/forecast/$1,$2
temp=$( cat $1,$2 | grep -E "<span class=\"summary swap\">*.*</span>")
#echo $temp
#<span class="summary swap">54˚&nbsp;Overcast.</span>
i=0
while [ $i -lt ${#temp} ] && [ "${temp:$i:1}" != ">" ] ; do
	(( i++ ))
done
(( i++ ))
temperature=""
while [ $i -lt ${#temp} ] && [ "${temp:$i:1}" != "&" ] ; do
	temperature="${temperature}${temp:$i:1}"
	(( i++ ))
done
(( i+=6 ))
weather=""
while [ $i -lt ${#temp} ] && [ "${temp:$i:1}" != "<" ] ; do
	weather="${weather}${temp:$i:1}"
	(( i++ ))
done
echo "Temperature is $temperature"
echo "Weather is $weather"
rm $1,$2
