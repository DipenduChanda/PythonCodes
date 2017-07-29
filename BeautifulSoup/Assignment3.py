import urllib
from BeautifulSoup import *

#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
count = 1
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    if count == 18:
        print count 
        print 'URL:',tag.get('href', None)
        print 'Contents:',tag.contents[0]
        break
    count = count +1