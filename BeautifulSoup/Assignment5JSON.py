import urllib
import json

summ = 0
count = 0
address = 'http://python-data.dr-chuck.net/comments_319811.json'
#raw_input('Enter location: ')

uh = urllib.urlopen(address)
data = uh.read()
#print data
tree = json.loads(data)

#print json.dumps(tree, indent= 4)
for item in tree['comments']:
    count = count +1
    #print item['count']
    summ = summ + int(item['count'])
    #print item.find('count').text
print summ
print count
