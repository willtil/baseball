from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import unicodedata, re

url = 'http://games.espn.go.com/flb/leaders?leagueId=54879&teamId=11&seasonId=2014&startIndex=0&scoringPeriodId='
index = 1
r = requests.get(url+str(index))
c = r.content
soup = BeautifulSoup(c)
#f = open('html.txt','w')
#f.write(str(soup))
#f.close()


nameTags = soup.find_all('td',{'class':'playertablePlayerName'})
Names = []
p = re.compile('^.*?(?=,)')
for x in nameTags:
	y = p.match(unicodedata.normalize('NFKD', x.text).encode('ascii','ignore'))
	Names.append(y.group())

statsTags = soup.find_all('td',{'class':'playertableStat'})
q = re.compile(r"[+-]?\d+(?:\.\d+)?|--")
Stats = []
for x in statsTags:
	y = q.match(unicodedata.normalize('NFKD', x.text).encode('ascii','ignore'))
	if y:
		Stats.append(y.group())
print Stats


s = 16


	

#statsTags = soup.find_all('td',{'class':'playertableStat'})
#Stats = [x.text.encode('utf-8') for x in statsTags]
#print Stats