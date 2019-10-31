# Why scrapping
# Have access to information on the web
#Can be done using a Library called beautiful soup
# If you're looking for  an update on the information 

import urllib.parse,urllib.request, urllib.error 
from bs4 import BeautifulSoup
import ssl

url = input('Enter -->:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

#Retrieve all of the anchor tags

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))