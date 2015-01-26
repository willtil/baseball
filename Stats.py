from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import unicodedata, re


PointsDict = {}
for index in [1,9,10]:
#URL for ESPN fantasy baseball top performers. Will need some work - this looks at the top 50 players for a particular day. Days are appended to the end of the URL by the "index" variable.
	url = 'http://games.espn.go.com/flb/leaders?leagueId=54879&teamId=11&seasonId=2014&startIndex=0&scoringPeriodId='
	#index = 1
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
	
	multiple = len(Stats)/16
	totalpointsindex = [15*(x+1) for x in range(multiple)]
	totalpoints = [Stats[x] for x in totalpointsindex]
	
	#d = dict(zip(Names,totalpoints))
	#print d
	z = zip(Names,totalpoints)
	for (name, points) in z:
		if points != '-':
			if points != '--':
				digit = int(points)
				if name in PointsDict:
					PointsDict[name].append(digit)
				else:
					PointsDict[name] = [digit]
	print len(PointsDict)
print PointsDict

#statsTags = soup.find_all('td',{'class':'playertableStat'})
#Stats = [x.text.encode('utf-8') for x in statsTags]
#print Stats