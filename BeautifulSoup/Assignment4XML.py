import urllib
import xml.etree.ElementTree as ET

summ = 0
count = 0
address = 'http://python-data.dr-chuck.net/comments_319807.xml'
#'http://python-data.dr-chuck.net/comments_42.xml'
#raw_input('Enter location: ')

uh = urllib.urlopen(address)
data = uh.read()
#print data
tree = ET.fromstring(data)


lst = tree.findall('comments/comment')

for item in lst:
    count = count +1
    summ = summ + int(item.find('count').text)
    #print item.find('count').text
print summ
print count
