import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


#Ignore ssl certs errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url -->:')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')


#Retrieve the html
count = 0
tags = soup('a')
for tag in tags:
    count[tag] += 1 
    print(tag.get('href',None))
    count[tag] += 1

    print(count)

#filerd