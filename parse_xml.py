import urllib
import xml.etree.ElementTree as ET

url=raw_input('Enter location: ')
data=urllib.urlopen(url).read()
print 'Retrieving '+url
print 'Retrieved '+str(len(data)) +' characters'
tree=ET.fromstring(data)

results=tree.findall('.//count')
print 'Count: '+str(len(results))
sum=0
for i in results:
	sum+= int(i.text)


print 'Sum: '+str(sum)	
