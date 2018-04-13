a = open('privateIPLists.txt','r')
ip = []

for line in a:
	i = line.rstrip()
	ip.append(i)
 
print ip
print len(ip)
