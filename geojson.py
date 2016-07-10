import urllib
import json

url='http://python-data.dr-chuck.net/geojson?'
address=raw_input('Enter location: ')

url=url+urllib.urlencode({'sensor':'false','address':address})

print 'Retrieving',url
data=urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'
try:js=json.loads(data)
except:js=None
if 'status' not in js or js['status']!='OK':
	print 'fail'
	print data
else:	
	#print json.dumps(js,indent=4)
	print js['results'][0]['place_id']
