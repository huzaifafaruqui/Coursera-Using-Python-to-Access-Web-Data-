import json
import urllib

url=raw_input('Enter location: ')
print 'Retrieving',url
data=urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'

fData=json.loads(data)
tsum=0
for item in fData['comments']:
	tsum+=int(item['count'])
print tsum	
#print fData
