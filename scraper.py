from __future__ import print_function
from bs4 import BeautifulSoup
import urllib2
import csv

#Insert url with tables below
url='example.com'
soup = BeautifulSoup(urllib2.urlopen(url).read())

f = open('datafile','w')

tables = soup.findAll('table', attrs={'class': 'table'})
for table in tables:
	rows = table.findAll('tr')
	for tr in rows:
		cols = tr.findAll('td')
		for td in cols:
			#Insert correct charset below (current: cp1252=windows-1252)
			f.write(td.text.encode('cp1252'))
			f.write(';')
f.close()
