import requests 

f = open("mobile_data.txt","w")#output file containing scrapped data
url_list = []
from bs4 import BeautifulSoup 
URL = "https://www.gsmarena.com"
r = requests.get(URL)
soup = BeautifulSoup(r.content,'html5lib')
for i in soup.find_all('div',{'class':'brandmenu-v2 light l-box clearfix'}):
	for j in i.find_all('li'):
		for k in j.find_all('a'):
			url = 'http://www.gsmarena.com/' + k.get('href')
			url_list.append(url)
			#print(url,"\n")

# for u in url_list:
# 	print(u)

phone_url_list = []

for url in url_list:
	r2 = requests.get(url)
	soup = BeautifulSoup(r2.content,'html5lib')
	for n in soup.find_all('div',{'class':'makers'}):
		for m in n.find_all('li'):
			for y in m.find_all('a'):
				print("hi")
				phone_url = 'http://www.gsmarena.com/'+ y.get('href')
				phone_url_list.append(phone_url)			

count = 0
for phone in phone_url_list:
	count = count + 1
	print(count)
	r3 = requests.get(phone)
	soup3 = BeautifulSoup(r3.content,'html5lib')
	model = soup3.find('h1',{'class':'specs-phone-name-title'}).text
	print("Model       : ",model)
	try:
		os=soup3.find('td',attrs={'data-spec':'os'}).text
	except:
		os="Blank"
	print("OS          : ",os)
	f.write("OS          : ")
	f.write(os)
	f.write("\n")
	try:
		cpu=soup3.find('td',attrs={'data-spec':'cpu'}).text
	except:
		cpu="Blank"
	print("CPU         : ",cpu)
	f.write("CPU         : ")
	f.write(cpu)
	f.write("\n")
	try:
		gpu=soup3.find('td',attrs={'data-spec':'gpu'}).text
	except:
		gpu="Blank"
	print("GPU         : ",gpu)
	f.write("GPU         : ")
	f.write(gpu)
	f.write("\n")
	try:
		dim=soup3.find('td',attrs={'data-spec':'dimensions'}).text
	except:
		dim="Blank"
	print("Dimensions  : ",dim)
	f.write("Dimensions  : ")
	f.write(dim)
	f.write("\n")
	try:
		mem=soup3.find('td',attrs={'data-spec':'internalmemory'}).text
	except:
		mem="Blank"
	print("Memory      : ",mem)
	f.write("Memory      : ")
	f.write(mem)
	f.write("\n")
	try:
		resol=soup3.find('td',attrs={'data-spec':'displayresolution'}).text
	except:
		resol="Blank"
	print("Resolution  : ",resol)
	f.write("Resolution  : ")
	f.write(resol)
	f.write("\n")
	try:
		sensors=soup3.find('td',attrs={'data-spec':'sensors'}).text
	except:
		sensors="Blank"
	print("Sensors     : ",sensors)
	f.write("Sensors     : ")
	f.write(sensors)
	f.write("\n")
	try:
		vid=soup3.find('td',attrs={'data-spec':'cam1video'}).text
	except:
		vid="Blank"
	print("Video       : ",vid)
	f.write("Video       : ")
	f.write(vid)
	f.write("\n")
	try:
		cardslot=soup3.find('td',attrs={'data-spec':'memoryslot'}).text
	except:
		cardslot="Blank"
	print("Card Slot   : ",cardslot,"\n\n")
	f.write("Card Slot   : ")
	f.write(cardslot)
	f.write("\n\n")



			#print(phone_url,"\n")


			

