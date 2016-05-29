import urllib
from BeautifulSoup import *
url=raw_input('Enter - ')
i=0
while i<8:
	html=urllib.urlopen(url).read()
	print 'Retrieving:',url
	soup=BeautifulSoup(html)
	tags=soup('a')
	url=tags[17].get('href',None)
	i+=1
