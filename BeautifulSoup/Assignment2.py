#http://python-data.dr-chuck.net/comments_42.html
import urllib
import re
from BeautifulSoup import *

#url = raw_input('Enter - ')
#url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_319810.html'
html = urllib.urlopen(url).read()
count = 0
sum = 0
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    count = count + 1
    y = str(tag)
    #print type(y)
    y= re.findall('[0-9]+', y)
    sum = sum+ int(y[0])
    #sum = sum + int(tag.get('span', None))
    #if (len(tag)==1):
        #print tag.rsplit('ts">')[1].rsplit('</span')[0]
        #print re.search('ts">(.+)</span', tag).group(1)
    #print 'TAG:',tag
    #print type(tag)
print count
print sum