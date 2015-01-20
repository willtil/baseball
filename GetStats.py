from urllib2 import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import csv
import unicodedata


def GetStats(soup):

	statsTags = soup.find_all('td',{'class':'playertableStat'})
	Stats = [str(x.text) for x in statsTags]

	return Stats

def GetRoster(soup):
	
	nameTags = soup.find_all('td',{'class':'playertablePlayerName'})
	Names = []
	for x in nameTags:
		y = unicodedata.normalize('NFKD', x.text).encode('ascii','ignore')
		Names.append(y)

	return Names



teams = [1, 6, 7, 8, 9, 10, 11, 12, 13, 14]
roster = {}
#for x in teams:
#	roster[x] = GetRoster(x)

url = urlopen('http://games.espn.go.com/flb/clubhouse?leagueId=54879&teamId=11&seasonId=2014&scoringPeriodId=164&view=stats&context=clubhouse&version=currSeason&ajaxPath=playertable/prebuilt/manageroster&managingIr=false&droppingPlayers=false&asLM=false')
soup = BeautifulSoup(url)

roster = GetRoster(soup)
stats = GetStats(soup)

cols = []
data = []

for d in stats:
	if re.match('\dB', d): 
		cols.append(d)
	elif re.match('\d|-', d):
		data.append(d)
	else:
		cols.append(d)	

print cols
print data


#df = pd.DataFrame()