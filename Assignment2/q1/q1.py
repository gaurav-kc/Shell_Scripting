import random

f=open("ipl_auctions_dataset.txt","r")
data = f.readlines()
f.close()
indian_bowlers = []
indian_batsman = []
indian_allrounder = []
indian_wicketkeep = []
over_bowlers = []
over_batsman = []
over_allrounder = []
over_wicketkeep = []
class player:
    def __init__(self,name,country,ability,fees):
        self.name = name
        self.country = country
        self.ability = ability
        self.fees = fees
    def getName(self):
        return self.name
    def getCountry(self):
        return self.country
    def getAbility(self):
        return self.ability
    def getFees(self):
        return self.fees
for i in data:
    temp = i.split(":")
    name = temp[0]
    country = temp[1]
    ability = temp[2]
    fees = temp[3]
    player_obj = player(name,country,ability,fees)
    if country == "India":
        if ability == "Bowler":
            indian_bowlers.append(player_obj)
        if ability == "Batsman":
            indian_batsman.append(player_obj)
        if ability == "All-Rounder":
            indian_allrounder.append(player_obj)
        if ability == "Wicket Keeper":
            indian_wicketkeep.append(player_obj)
    else:
        if ability == "Bowler":
            over_bowlers.append(player_obj)
        if ability == "Batsman":
            over_batsman.append(player_obj)
        if ability == "All-Rounder":
            over_allrounder.append(player_obj)
        if ability == "Wicket Keeper":
            over_wicketkeep.append(player_obj)
fconfig=open("config.txt","r")
overseas = fconfig.readline()
temp = overseas.split(":")
overseas_low = int(temp[1])
overseas_high = int(temp[2])
bowlers = fconfig.readline()
temp = bowlers.split(":")
bowlers_low = int(temp[1])
bowlers_high = int(temp[2])
batsmen = fconfig.readline()
temp = batsmen.split(":")
batsmen_low = int(temp[1])
batsmen_high = int(temp[2])
wicketkeeper = fconfig.readline()
temp = wicketkeeper.split(":")
wicketkeeper_low = int(temp[1])
wicketkeeper_high = int(temp[2])
allrounders = fconfig.readline()
temp = allrounders.split(":")
allrounders_low = int(temp[1])
allrounders_high = int(temp[2])
teams = fconfig.readline()
temp = teams.split(":")
team_count = int(temp[1])
temp = fconfig.readline()
team_names = []
for i in range(0,team_count):
    team_names.append(fconfig.readline().rstrip('\n'))
fconfig.close()
class stats:
    def __init__(self):
        self.batsman = 0
        self.bowlers = 0
        self.wicketkeeper = 0
        self.allrounders = 0
        self.overseas = 0
    def incbatsman(self):
        self.batsman = self.batsman+1
    def incbowler(self):
        self.bowlers = self.bowlers+1
    def incwicketkeeper(self):
        self.wicketkeeper = self.wicketkeeper+1
    def incallrounder(self):
        self.allrounders = self.allrounders+1
    def incoverseas(self):
        self.overseas = self.overseas+1
    def isMinBatsman(self):
        if self.batsman >= batsmen_low:
            return True
        return False
    def isMinBowlers(self):
        if self.bowlers >= bowlers_low:
            return True
        return False
    def isMinWicket(self):
        if self.wicketkeeper >= wicketkeeper_low:
            return True
        return False
    def isMinAllrounder(self):
        if self.allrounders >= allrounders_low:
            return True
        return False
    def isMinOverseas(self):
        if self.overseas >= overseas_low:
            return True
        return False
    def isMaxBatsman(self):
        if self.batsman == batsmen_high:
            return True
        return False
    def isMaxBowlers(self):
        if self.bowlers == bowlers_high:
            return True
        return False
    def isMaxWicket(self):
        if self.wicketkeeper == wicketkeeper_high:
            return True
        return False
    def isMaxAllrounder(self):
        if self.allrounders == allrounders_high:
            return True
        return False
    def isMaxOverseas(self):
        if self.overseas == overseas_high:
            return True
        return False
    
    
    
class team:
    def __init__(self):
        player_list=[]
        self.player_list = player_list
        stats_obj = stats()
        self.stats_obj = stats_obj
    def getBowlerCount(self):
        return self.stats_obj.bowlers
    def getBatsmanCount(self):
        return self.stats_obj.batsman
    def getWicketCount(self):
        return self.stats_obj.wicketkeeper
    def getAllRounderCount(self):
        return self.stats_obj.allrounders
    def getPlayerCount(self ):
        return len(self.player_list)
    def getOverseasCount(self):
        return self.stats_obj.overseas
#some functions on lists
def removeIndianPlayer(playername):
    for i in indian_batsman:
        if i.getName() == playername:
            indian_batsman.remove(i)
    for i in indian_bowlers:
        if i.getName() == playername:
            indian_bowlers.remove(i)
    for i in indian_wicketkeep:
        if i.getName() == playername:
            indian_wicketkeep.remove(i)
    for i in indian_allrounder:
        if i.getName() == playername:
            indian_allrounder.remove(i)

def removeOverseasPlayer(playername):
    for i in over_batsman:
        if i.getName() == playername:
            over_batsman.remove(i)
    for i in over_bowlers:
        if i.getName() == playername:
            over_bowlers.remove(i)
    for i in over_wicketkeep:
        if i.getName() == playername:
            over_wicketkeep.remove(i)
    for i in over_allrounder:
        if i.getName() == playername:
            over_allrounder.remove(i)

team_list = []
for i in range(0,team_count):
    team_obj = team()
    team_list.append(team_obj)
def printStats():
    print "ind bow ",len(indian_bowlers)
    print "ind bats ",len(indian_batsman)
    print "ind wicket ",len(indian_wicketkeep)
    print "ind allround ",len(indian_allrounder)
    print "over bow ",len(over_bowlers)
    print "over bats ",len(over_batsman)
    print "over wicket ",len(over_wicketkeep)
    print "over allround ",len(over_allrounder)

min_bow_required = team_count*bowlers_low
min_bat_required = team_count*batsmen_low
min_wic_required = team_count*wicketkeeper_low
min_all_required = team_count*allrounders_low
min_ove_required = team_count*overseas_low
def printMin():
    print "min bow ",min_bow_required
    print "min bat ",min_bat_required
    print "min wic ",min_wic_required
    print "min all ",min_all_required
    print "min over ",min_ove_required
#printStats()
#printMin()
#logic for this particular example
flag = True
team_number = 0
while(team_number != team_count):
    while team_list[team_number].stats_obj.isMinBowlers() == False:
        temp = random.choice(over_bowlers)
        team_list[team_number].player_list.append(temp)
        removeOverseasPlayer(temp.getName())
        team_list[team_number].stats_obj.incbowler()
        team_list[team_number].stats_obj.incoverseas()
    team_number = team_number + 1

team_number = 0
while(team_number != team_count):
    while team_list[team_number].stats_obj.isMinBatsman() == False:
        temp = random.choice(indian_batsman)
        team_list[team_number].player_list.append(temp)
        removeIndianPlayer(temp.getName())
        team_list[team_number].stats_obj.incbatsman()
    team_number = team_number + 1

team_number = 0
while(team_number != team_count):
    while team_list[team_number].stats_obj.isMinWicket() == False:
        temp = random.choice(indian_wicketkeep)
        team_list[team_number].player_list.append(temp)
        removeIndianPlayer(temp.getName())
        team_list[team_number].stats_obj.incwicketkeeper()
    team_number = team_number + 1

team_number = 0
while(team_number != team_count):
    while team_list[team_number].stats_obj.isMinAllrounder() == False:
        temp = random.choice(over_allrounder)
        team_list[team_number].player_list.append(temp)
        removeOverseasPlayer(temp.getName())
        team_list[team_number].stats_obj.incallrounder()
    team_number = team_number + 1  

#printStats()

flag = True
team_number = 0
while(team_number != team_count):
    for i in range(0,2):
        temp = random.choice(over_batsman)
        team_list[team_number].player_list.append(temp)
        removeOverseasPlayer(temp.getName())
        team_list[team_number].stats_obj.incbatsman()
        team_list[team_number].stats_obj.incoverseas()
    for i in range(0,2):
        temp = random.choice(indian_bowlers)
        team_list[team_number].player_list.append(temp)
        removeIndianPlayer(temp.getName())
        team_list[team_number].stats_obj.incbowler()
    for i in range(0,2):
        temp = random.choice(indian_allrounder)
        team_list[team_number].player_list.append(temp)
        removeIndianPlayer(temp.getName())
        team_list[team_number].stats_obj.incallrounder
    team_number = team_number+1

def checkConstraintSatisfaction():
    for i in team_list:
        if i.getOverseasCount() < overseas_low or i.getOverseasCount() > overseas_high:
            print "Error in overseas"
            exit()
        if i.getBowlerCount() < bowlers_low or i.getBowlerCount() > bowlers_high:
            print "Error in bowlers"
            exit()
        if i.getBatsmanCount() < batsmen_low or i.getBatsmanCount() > batsmen_high:
            print "Error in batsman"
            exit()
        if i.getWicketCount() < wicketkeeper_low or i.getWicketCount() > wicketkeeper_high:
            print "Error in wicketkeeper"
            exit()
        if i.getAllRounderCount() < allrounders_low or i.getAllRounderCount() > allrounders_high:
            print "Error in All rounders"
            exit()
        if i.getPlayerCount() != 18:
            print "Error in size of teams"
            exit()

checkConstraintSatisfaction()

for i in range(0,team_count):
    filename = team_names[i]
    filename = filename
    ftemp = open(filename + ".txt","w")
    ftemp.write(filename)
    ftemp.write("\n")
    k=1
    for j in team_list[i].player_list:
        ftemp.write("\nPlayer "+str(k))
        ftemp.write("\nName : "+ j.name)
        ftemp.write("\nCountry : "+ j.country)
        ftemp.write("\nAbility : " + j.ability)
        ftemp.write("\nFees : " + j.fees)
        ftemp.write("\n")
        k=k+1
    ftemp.close()
    
