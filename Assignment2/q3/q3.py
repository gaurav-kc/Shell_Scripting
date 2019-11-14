from pycricbuzz import Cricbuzz
from playsound import playsound
import json

cric = Cricbuzz()
match = cric.matches()

for k in match:
	print("Match id is ",k['id'])
	print("Match name is ",k['srs'])
	print("Match format is ",k['type'],"\n\n")

matchID=str(input("Enter matchID : "))

a=1

#print(comm['commentary'])
while True:
	abc=cric.commentary(matchID)
	#comm=cric.commentary(matchID)
	if(abc['commentary'][0]['comm'].find("SIX") != -1 and a!=len(abc['commentary'])):
		print(abc['commentary'][0]['comm'])
		playsound('six.mp3')
		a = len(abc['commentary'])	
	elif(abc['commentary'][0]['comm'].find("FOUR") != -1 and a!=len(abc['commentary'])):
		print(abc['commentary'][0]['comm'])
		playsound('four.mp3')
		a = len(abc['commentary'])	
	elif(abc['commentary'][0]['comm'].find("THATS OUT") != -1 and a!=len(abc['commentary'])):
		print(abc['commentary'][0]['comm'])
		playsound('out.mp3')
		a = len(abc['commentary'])
	else:
		print(abc['commentary'][0]['comm'])			



