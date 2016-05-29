import re
f=open("regex_sum_278368.txt")
sum=0
for line in f:
	y=re.findall('[0-9]+',line)
	for x in y:
		sum+=int(x)
print sum
f.close()		
